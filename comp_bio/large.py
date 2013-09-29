import random
import copy
import time

n_conf = 0 	##Stores the number of conformations found for a particular string.
path=[] 			##Stores the path to be followed for a particular conformation.
save = [] 			##Stores the conformation with the minimum energy.
min_energy = 1 		##Stores the current minimum energy.
min_path = [] 
in_string = raw_input("Enter string:")
in_string = in_string.upper()
length = len(in_string)
side = 2*length + 1 
matrix = [['.' for x in xrange(side)] for x in xrange(side)] #Creates the lattice
histogram = [0 for x in xrange(20)] #Stores values for histogram.
conformations = [] ##Saves the current generation of conformations
count = 0	##Temporary variable used to maintain a count of processed letters 
			##in input.


xpos = ypos = length##xpos and ypos denote the current position in the lattice. Initialized
					##to the center of the lattice.

matrix[ypos][xpos] = in_string[count] ##Enters the first letter of the string into the lattice
count += 1 							  ##and increments the count by 1. Count is incremented everytime 
									  ##a letter from the string is entered into the lattice.
directions = 'UDLR'

def mat_dir(s):
	## This function updates the matrix. It takes two variables as arguments.
	global matrix, xpos, ypos, count
	if s=='U':
		if matrix[ypos-1][xpos] == '.':
			matrix[ypos-1][xpos] = in_string[count]
			ypos -= 1
			return 0
		return 1
	elif s=='D':
		if matrix[ypos+1][xpos] == '.':
			matrix[ypos+1][xpos] = in_string[count]
			ypos += 1
			return 0
		return 1
	elif s=='L':
		if matrix[ypos][xpos-1] == '.':
			matrix[ypos][xpos-1] = in_string[count]
			xpos -= 1
			return 0
		return 1
	elif s=='R':
		if matrix[ypos][xpos+1] == '.':
			matrix[ypos][xpos+1] = in_string[count]
			xpos += 1
			return 0
		return 1

def initialize(size=1000):
	global matrix, in_string, xpos, ypos
	for i in xrange(size):
		
		matrix[ypos][xpos] = in_string[count]
		count += 1
		for i in xrange(1, length):
			s = random.choice(directions)
			flag = mat_dir()



