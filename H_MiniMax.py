import copy
from state import*

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

def evalFunction(currentState):
	#a dict containing rienfield values for each piece
	r_values = {'P' : 1, 'K' : 3, 'B' : 3, 'R' : 5, 'Q' : 9, 'p' : -1, 'k' : -3, 'b' : -3, 'r' : -5, 'q' : -9 ,'_' : 0,'K' : 10000, 'k': -10000}
	function_sum = 0
	matrix = currentState.getMatrix()
	for row in matrix:
		for value in row:
			function_sum += r_values[value]
	return function_sum



def validMoves(currentState, posFrom):
	#conditional statements that returns an array of tuples, each one containing all
	#possible positions the piece can move to. For example, for a white knight on the starting
	#board at (7,2), it will return [(5,3),(5,1)] etc.
	matrix = currentState.getMatrix()

	x = posFrom[0]
	y = posFrom[1]
	moves = []
	if matrix[y][x] == 'P':
		if (y > 0):
			if matrix[y-1][x] == '_': #move straight
				moves.append(tuple([x,y-1]))
			if (x >0):
				if matrix[y-1][x-1] != '_' and matrix[y-1][x-1].islower(): #attack left
					moves.append(tuple([x-1,y-1]))
			if (x<7):
				if matrix[y-1][x+1] != '_' and matrix[y-1][x+1].islower(): #attack right
					moves.append(tuple([x+1,y-1]))

	elif matrix[y][x] == 'p':
		if (y < 7):
			if matrix[y+1][x] == '_': #move straight
				moves.append(tuple([x,y+1]))
			if (x >0):
				if matrix[y+1][x-1] != '_' and matrix[y+1][x-1].isupper(): #attack left
					moves.append(tuple([x-1,y+1]))
			if (x < 7):
				if matrix[y+1][x+1] != '_' and matrix[y+1][x+1].isupper(): #attack right
					moves.append(tuple([x+1,y+1]))

	#add more for each piece. 
	#Note: it will be the same for both white and black for pieces other than the pawn.
	return moves


#moves the piece and updates state accordingly
def move(currentState, posFrom, posTo):
	x = posFrom[0]
	y = posFrom[1]

	temp_matrix = copy.deepcopy(currentState.getMatrix())

	temp_matrix[posTo[1]][posTo[0]] = temp_matrix[y][x]
	temp_matrix[y][x] = '_'

	new_State = (currentState,temp_matrix,currentState.nextTurn(),(currentState.getDepth() +1 ) )

	return new_State

def explore1(currentState):
	#returns a list of tuples with x,y coordinates of all of the players pieces
	pieces = []
	turn = currentState.getTurn()
	x = 0
	y = 0 
	for row in currentState.getMatrix():
		x = 0
		for value in row:
			if turn == 'white':
				if value.isupper():
					pieces.append((x,y))
			else:
				if value.islower():
					pieces.append((x,y))		
			x+=1
		y+=1

	return pieces

def alpha_beta_max(currentState, alpha, beta, depth):
	if depth == 5:
		return evalFunction(currentState)
	for piece in explore1(currentState):
		for possibleMove in validMoves(currentState,piece):
			nextState = move(currentState,piece,possibleMove)
			score = alpha_beta_min(nextState, alpha, beta, depth + 1)

			if( score >= beta ):
				return beta #beta-cutoff
			if( score > alpha ):
				alpha = score #alpha keeps the maximum value from child
 	
	return alpha



def alpha_beta_min(State, alpha, beta, depth):
	return

def runGame(matrix):
		#deep copy
		#call move methods based on piece
		#get deep copy returned 
		#add to list of successors
		#once all successor states reached 
		#return list of successors. 
	currentState = State(None,matrix,'white',0)
	while True:
		currentState.display()

		#if either player wins, print a statement and quit 
		if(checkmate('white')):
			print('black player wins!')	
			return
		elif(checkmate('black')):
			print('white player wins!')
			return

		if currentState.getTurn() == 'white':
			pass

			#add code for AI
		else:
			#add code for user input and checks for validation
			pass
#def moveQueen(matrix, player, pos, blocks):

#def moveRook():

#def moveBishop():

#def moveKnight():

#look for checkmate of the player's king. Will make use of valid moves function for opponent pieces
def checkmate(player):
	#find position of the king

	#find valid positions of the king to move
	
	#loop through matrix and get validmoves from each piece.

	return False



print("Initial State A")
display(initialA)
print("")

InitialState = State(None,initialA,'black',0)
print("black pieces are on: ", end = ' ')
print(explore1(InitialState))

#print("Initial State B")
#display(initialB)
#print("")
#print("Initial State C")
#display(initialC)
#print("")
