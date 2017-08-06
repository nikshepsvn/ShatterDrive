# shatter.py is an implementation of Shamir's Secret Sharing Algorithm adapted to efficiently work on files.



#------------- SHARE COMPUTATION -------------#

with open("test.txt", "rb") as test:
  f = test.read()
  b = bytearray(f)

print (len(b))
