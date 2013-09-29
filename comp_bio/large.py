import random
import copy
import time

conformations = 0 	##Stores the number of conformations found for a particular string.
path=[] 			##Stores the path to be followed for a particular conformation.
save = [] 			##Stores the conformation with the minimum energy.
min_energy = 1 		##Stores the current minimum energy.
min_path = [] 
count = 0 			##Temporary variable used to maintain a count of processed letters 
					##in input.
in_string = raw_input("Enter string:")
in_string = in_string.upper()
length = len(in_string)
side = 2*length + 1 
matrix = [['.' for x in xrange(side)] for x in xrange(side)] #Creates the lattice
histogram = [0 for x in xrange(20)] #Stores values for histogram.

xpos = ypos = length##xpos and ypos denote the current position in the lattice. Initialized
					##to the center of the lattice.

matrix[ypos][xpos] = in_string[count] ##Enters the first letter of the string into the lattice
count += 1 							  ##and increments the count by 1. Count is incremented everytime 
									  ##a letter from the string is entered into the lattice.
directions = 'UDLR'

def initialize(size=1000):
	global directions, matrix, in_string
