import random
import copy
import time
import pdb

n_conf = 0 	##Stores the number of conformations found for a particular string.
path=[] 			##Stores the path to be followed for a particular conformation.
save = [] 			##Stores the conformation with the minimum energy.
min_energy = 1 		##Stores the current minimum energy.
min_path = [] 
in_string = raw_input("Enter string: ")
init_pop = int(raw_input("Enter size of initial population: "))
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

#matrix[ypos][xpos] = in_string[count] ##Enters the first letter of the string into the lattice
#count += 1 							  ##and increments the count by 1. Count is incremented everytime 
									  ##a letter from the string is entered into the lattice.
directions = 'UDLR'
energies = {}
def initialize(size=100):
	global matrix, in_string, xpos, ypos, count, conformations, energies
	i = 0
	while i < size:
		ypos = xpos = length
		matrix = [['.' for x in xrange(side)] for x in xrange(side)]
		matrix[ypos][xpos] = in_string[0]
		j = 1
		conformations.append('')
		energy = 0	
		while j<length:
			flag = 1
			while flag>0:
				s = random.choice(directions)
				if s=='U':
					if matrix[ypos-1][xpos] == '.':
						ypos -= 1
						matrix[ypos][xpos] = in_string[j]
						if in_string[count] == 'W':
			##Checking for W-W contacts:
							if matrix[ypos-1][xpos] == 'W':
								energy -= 1
							if matrix[ypos][xpos+1] == 'W':
								energy -= 1
							if matrix[ypos][xpos-1] == 'W':
								energy -= 1
						conformations[i] += s
						flag = 0
				elif s=='D':
					if matrix[ypos+1][xpos] == '.':
						ypos += 1
						matrix[ypos][xpos] = in_string[j]
						if in_string[count] == 'W':
						##Checking for W-W contacts:
							if matrix[ypos][xpos+1] == 'W':
								energy -= 1
							if matrix[ypos+1][xpos] == 'W':
								energy -= 1
							if matrix[ypos][xpos-1] == 'W':
								energy -= 1
						conformations[i] += s
						flag = 0
				elif s=='L':
					if matrix[ypos][xpos-1] == '.':
						xpos -= 1
						matrix[ypos][xpos] = in_string[j]
						if in_string[count] == 'W':
						##Checking for W-W contacts:
							if matrix[ypos-1][xpos] == 'W':
								energy -= 1
							if matrix[ypos][xpos-1] == 'W':
								energy -= 1
							if matrix[ypos+1][xpos] == 'W':
								energy -= 1
						conformations[i] += s
						flag = 0
				elif s=='R':
					if matrix[ypos][xpos+1] == '.':
						xpos += 1
						matrix[ypos][xpos] = in_string[j]
						if in_string[count] == 'W':
						##Checking for W-W contacts:
							if matrix[ypos-1][xpos] == 'W':
								energy -= 1
							if matrix[ypos][xpos+1] == 'W':
								energy -= 1
							if matrix[ypos+1][xpos] == 'W':
								energy -= 1
						conformations[i] += s
						flag = 0
			j += 1
		energies[conformations[i]]	= energy
		#pdb.set_trace()
		for k in xrange(side):
			print matrix[k]
		print "\n"
		i += 1


initialize(init_pop)
print conformations
print energies






