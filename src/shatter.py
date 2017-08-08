# shatter.py is an implementation of Shamir's Secret Sharing Algorithm adapted to efficiently work on files.
#------------- IMPORTS -------------#
from random import SystemRandom
random_gen = SystemRandom()

#------------- CONSTANTS -------------#

PATH = "test.txt"
BLOCK_SIZE = 1024

#------------- SHARE COMPUTATION -------------#

#function that returns a Cryptographically secure random number in between the ranges
def random_num(min, max):
    return random_gen.randint(min,max)

# read_file is a function that takes in the path of a file and reads the file in chunks of {block_size} bytes.
def read_chunks(path, block_size=1024):
    with open(path, 'rb') as f:
        while True:
            piece = f.read(block_size)
            if piece:
                yield bytearray(piece)
            else:
                return

#polynomial_gen is a function that takes in a number and generates a polynomial
def polynomial_gen(secret_bit, share_treshold):
    share_byte_list = []
    coeffecient = share_treshold - 1

    for x in range (0, coeffecient):
        share_byte_list.append(random_num(-128, 127))

    share_byte_list.append(secret_bit)

    return share_byte_list

# create_shard is a function that takes in a chunk of data and splits it into shares using SSSA
def create_pack_of_share_for_byte(piece, share_treshold, number_of_shares):
    pack_of_share_bytes = []

    for x in range (0, number_of_shares):
        pack_of_share_bytes.append(polynomial_gen(piece, share_treshold))

    return pack_of_share_bytes

def create_pack_of_shares(chunk, share_treshold, number_of_shares):
    pack_of_shares = []

    for x in chunk:
        pack_of_shares.append(create_pack_of_share_for_byte(x, share_treshold, number_of_shares))

    return pack_of_shares

#chunk_sharder is a function that coverts
def chunk_sharder (share_treshold, number_of_shares):
    pack_of_shares = []

    for chunk in read_chunks(PATH):
        pack_of_shares.append(create_pack_of_shares(chunk, share_treshold, number_of_shares))

    return pack_of_shares


print(chunk_sharder(3, 5)) # test statement
