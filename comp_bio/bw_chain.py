import copy
import time

conformations = 0 	##Stores the number of conformations found for a particular string.
path=[] 			##Stores the path to be followed for a particular conformation.
save = [] 			##Stores the conformation with the minimum energy.
min_energy = 1 		##Stores the current minimum energy.
min_path = [] 		##Stores the path for the conformation with min energy.
u=['U']; d=['D'] 	##for denoting path; U: UP, D:DOWN, L:LEFT, R: RIGHT.
l=['L']; r=['R'] 
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

def func(path,ypos,xpos,count,energy):
	global conformations, matrix, min_energy, min_path, save, histogram
	if count == length:
		##This code block is entered only when the entire 
		##string has been entered into the lattice. i.e this
		##is the control block for this recursive program.
		conformations += 1
		histogram[(-energy)] += 1
		if energy < min_energy:
			##IF a new minimum has been found.
			min_energy = energy
			save = copy.deepcopy(matrix)
			min_path = copy.deepcopy(path)
		return
	if matrix[ypos-1][xpos] == '.':
		##IF a position ABOVE the current position is empty in the lattice.
		ypos -= 1
		encount = 0 ##This count is maintained so that whenever the program backtracks
					##it can restore the energy variable to its previous state.
		matrix[ypos][xpos] = in_string[count]
		if in_string[count] == 'W':
			##Checking for W-W contacts:
			if matrix[ypos-1][xpos] == 'W':
				energy -= 1
				encount += 1
			if matrix[ypos][xpos+1] == 'W':
				energy -= 1
				encount += 1
			if matrix[ypos][xpos-1] == 'W':
				energy -= 1
				encount += 1
		##Recursive call.
		func(path+u,ypos,xpos,count+1,energy)
		##Restoring state for backtracking.
		matrix[ypos][xpos] = '.'
		energy += encount
		ypos += 1
	if matrix[ypos][xpos+1] == '.':
		##IF a position to the RIGHT of the current position is empty in the lattice.
		xpos += 1
		encount = 0 ##This count is maintained so that whenever the program backtracks
					##it can restore the energy variable to its previous state.
		matrix[ypos][xpos] = in_string[count]
		if in_string[count] == 'W':
			##Checking for W-W contacts:
			if matrix[ypos-1][xpos] == 'W':
				energy -= 1
				encount += 1
			if matrix[ypos][xpos+1] == 'W':
				energy -= 1
				encount += 1
			if matrix[ypos+1][xpos] == 'W':
				energy -= 1
				encount += 1
		##Recursive call.
		func(path+r,ypos,xpos,count+1,energy)
		##Restoring state for backtracking.
		matrix[ypos][xpos] = '.'
		xpos -= 1
		energy += encount
	if matrix[ypos+1][xpos] == '.':
		##IF a position BELOW the current position is empty in the lattice.
		ypos += 1
		encount = 0 ##This count is maintained so that whenever the program backtracks
					##it can restore the energy variable to its previous state.
		matrix[ypos][xpos] = in_string[count]
		if in_string[count] == 'W':
			##Checking for W-W contacts:
			if matrix[ypos][xpos+1] == 'W':
				energy -= 1
				encount += 1
			if matrix[ypos+1][xpos] == 'W':
				energy -= 1
				encount += 1
			if matrix[ypos][xpos-1] == 'W':
				energy -= 1
				encount += 1
		##Recursive call.
		func(path+d,ypos,xpos,count+1,energy)
		##Restoring state for backtracking.
		matrix[ypos][xpos] = '.'
		ypos -= 1
		energy += encount
	if matrix[ypos][xpos-1] == '.':
		##IF a position to the LEFT of the current position is empty in the lattice.
		xpos -= 1
		encount = 0 ##This count is maintained so that whenever the program backtracks
					##it can restore the energy variable to its previous state.
		matrix[ypos][xpos] = in_string[count]
		if in_string[count] == 'W':
			##Checking for W-W contacts:
			if matrix[ypos-1][xpos] == 'W':
				energy -= 1
				encount += 1
			if matrix[ypos][xpos-1] == 'W':
				energy -= 1
				encount += 1
			if matrix[ypos+1][xpos] == 'W':
				energy -= 1
				encount += 1
		##Recursive call.
		func(path+l,ypos,xpos,count+1,energy)
		##Restoring state for backtracking.
		energy += encount
		matrix[ypos][xpos] = '.'
		xpos -= 1

##Starting the clock for calculating time
start_time = time.time()
func(path,ypos,xpos,count,0) ##Initial function call
end_time = time.time() ##Stopping the clock
total_time = end_time - start_time

print "Conformations: ",conformations
print "Conformation with minimum energy:"
for i in xrange(side):
	print save[i]
print "\n"
print "Energy: ",min_energy
print "Path: ",min_path
print "Time: ",total_time
print "Histogram: ",histogram