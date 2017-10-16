# shatter.py is an implementation of Shamir's Secret Sharing Algorithm adapted to efficiently work on files.
#------------- IMPORTS -------------#

from random import SystemRandom
from scipy import interpolate
import numpy as np

# instantiating SystemRandom as randomgen
random_gen = SystemRandom()


#------------- CONSTANTS -------------#

PATH = "test.txt" #location of file to shatter
BLOCK_SIZE = 1024 #Currently set at 1024 bytes, ie. 1MB chunks

#------------- SHARE COMPUTATION -------------#

#function that returns a Cryptographically secure random number in between the ranges
def random_num(min, max):
	return random_gen.randint(min,max)

#read_file is a function that takes in the path of a file and reads the file in chunks of {block_size} bytes of type bypearray.
def read_data_in_chunks(PATH, BLOCK_SIZE):
	with open(PATH, 'rb') as f:
		while True:
			piece = f.read(BLOCK_SIZE)
			if piece:
				yield bytearray(piece)
			else:
				return

#polynomial_gen is a function that takes in a number and generates a polynomial
def polynomial_gen(secret, threshold):
	coeffecient = threshold - 1
	coefficient_list = []

	for x in range (0, coeffecient): #loop generates the co-effients for the poloynomials
		coefficient_list.append(random_num(-128, 127))

	coefficient_list.append(secret)

	return coefficient_list #this contains all the co-effients from the polynomials, 
							#ie. if a polynomial is in the form of y=ax^2+bx+c, then coefficient_list = [a,b,c]

def get_points_from_polynomial (coefficient_list, threshold, shares):
	array_of_points = []
	x_points = []
	y_points = []

	for j in range(0, shares):
		x = random_num(-128,127)
		y = 0
		for i in range (1, threshold+1):
			y = y + coefficient_list[i-1]*x**(threshold-i)
		x_points.append(x)
		y_points.append(y)
		array_of_points.append([x,y])

	return [x_points, y_points]

def generate_points_with_secret_shares_and_threshold(secret, threshold, shares):
	return get_points_from_polynomial(polynomial_gen(secret, threshold), threshold, shares)

def reconstruct_secret(x_points, y_points):
	return np.rint(interpolate.barycentric_interpolate(x, y, 0))
