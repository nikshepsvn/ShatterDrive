# shatter.py is an implementation of Shamir's Secret Sharing Algorithm adapted to efficiently work on files.



#------------- SHARE COMPUTATION -------------#

def read_file(path, block_size=1024):
    with open(path, 'rb') as f:
        while True:
            piece = f.read(block_size)
            if piece:
                yield piece
            else:
                return

for piece in read_file('test.txt'):
    print(piece)
