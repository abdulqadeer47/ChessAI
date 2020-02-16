initialA = [['_','_','_','_','_','_','q','k'],['_','_','_','_','_','_','_','_'],['_','_','_','_','_','P','_','p'],['_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','_','_'],['_','_','_','_','_','_','Q','P'],['_','_','_','_','_','P','P','_'],['_','_','_','_','R','_','K','_']]
initialB = [['_','_','B','_','_','_','_','_'],['_','_','_','_','_','_','_','_'],['_','_','_','K','_','_','_','_'],['_','p','_','_','_','_','_','_'],['_','_','k','_','_','_','_','_'],['P','_','_','_','_','P','_','_'],['_','B','_','_','_','_','_','_'],['N','_','_','_','_','N','_','_']]
initialC = [['_','_','_','_','_','_','_','_'],['_','_','_','K','_','_','_','_'],['_','_','R','_','P','_','_','_'],['_','P','_','k','r','_','_','_'],['_','_','_','N','p','b','_','_'],['_','_','_','_','P','_','_','_'],['_','_','_','_','_','_','_','_'],['_','_','_','_','_','N','_','_']]

###########################################################	
# Display method:                                         #
# prints out the given 2d matrix to the console			  #
# Paramters:                                              #
# 1) matrix: 2d array to print to console  				  #
###########################################################
def display(matrix):
	for row in matrix:
		for value in row:
			print(value, end = ' ')
		print("")

def evalFunction(matrix):
	Q = 9
	R = 5
	B = 3
	K = 3
	P = 1
	q
	for row in matrix:
		for value in row:
			if(value == 'Q'):

			elif(value == 'R'):

			elif(value == 'B' or value == 'K'):

			elif(value == 'P'): 
	return 0



def action(matrix, player):
	if (player == 'white'):

		#deep copy
		#call move methods based on piece
		#get deep copy returned 
		#add to list of successors
		#once all successor states reached 
		#return list of successors. 

def movePawn(matrix, player, pos):
	x = pos[0]
	y = pos[1]

	if( player == white):

	#else black
	else:

	return matrix

def moveQueen():

def moveRook():

def moveBishop():

def moveKnight():




print("Initial State A")
display(initialA)
print("")
print("Initial State B")
display(initialB)
print("")
print("Initial State C")
display(initialC)
print("")
