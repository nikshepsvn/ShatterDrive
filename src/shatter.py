# shatter.py is an implementation of Shamir's Secret Sharing Algorithm adapted to efficiently work on files.
#------------- IMPORTS -------------#
from random import SystemRandom


#------------- CONSTANTS -------------#

PATH = "test.txt"

#------------- SHARE COMPUTATION -------------#

# sharder is a function that takes in a chunk of data and splits it into shares using SSSA
def create_shard(data, share_treshold):
    print(data)

# read_file is a function that takes in the path of a file and reads the file in chunks of {block_size} bytes.
def read_file(path, block_size=1024):
    with open(path, 'rb') as f:
        while True:
            piece = f.read(block_size)
            if piece:
                yield piece
            else:
                return

#process_data is currently a placeholder function name for the function that will be actually handling the piece recieved
for piece in read_file(PATH):
    create_shard(bytearray(piece))
