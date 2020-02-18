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
	r_values = {'P' : 1, 'N' : 3, 'B' : 3, 'R' : 5, 'Q' : 9, 'p' : -1, 'n' : -3, 'b' : -3, 'r' : -5, 'q' : -9 ,'_' : 0,'K' : 10000, 'k': -10000}
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
	player = currentState.getTurn()
	x = posFrom[0]
	y = posFrom[1]
	moves = []
	if matrix[y][x] == 'P' and player == 'white':
		if (y > 0):
			if matrix[y-1][x] == '_': #move straight
				moves.append(tuple([x,y-1]))
			if (x >0):
				if matrix[y-1][x-1] != '_' and matrix[y-1][x-1].islower(): #attack left
					moves.append(tuple([x-1,y-1]))
			if (x<7):
				if matrix[y-1][x+1] != '_' and matrix[y-1][x+1].islower(): #attack right
					moves.append(tuple([x+1,y-1]))

	elif matrix[y][x] == 'p' and player == 'black':
		if (y < 7):
			if matrix[y+1][x] == '_': #move straight
				moves.append(tuple([x,y+1]))
			if (x >0):
				if matrix[y+1][x-1] != '_' and matrix[y+1][x-1].isupper(): #attack left
					moves.append(tuple([x-1,y+1]))
			if (x < 7):
				if matrix[y+1][x+1] != '_' and matrix[y+1][x+1].isupper(): #attack right
					moves.append(tuple([x+1,y+1]))
	#for white king
	elif matrix[y][x] == 'K' and player == 'white' :
		for i in range(x-1,x+2):
			if i >= 0 and i <=7: 
				for j in range(y-1,y+2):
					if j >=0 and j <= 7:
						if not matrix[j][i].isupper():
							moves.append((i,j))
	#for black king						
	elif matrix[y][x] == 'k' and player == 'black' :
		for i in range(x-1,x+2):
			if i >= 0 and i <=7: 
				for j in range(y-1,y+2):
					if j >=0 and j <= 7:
						if not matrix[j][i].islower():
							moves.append((i,j))
	#for white rook
	elif matrix[y][x] == 'R' and player == 'white':
		for j in range(y-1,-1,-1):
			if not matrix[j][x].isupper():
				moves.append((x,j))
			else:
				break
		for j in range(y+1,8):
			if not matrix[j][x].isupper():
				moves.append((x,j))
			else:
				break
		for i in range(x-1,-1,-1):
			if not matrix[y][i].isupper():
				moves.append((i,y))
			else:
				break
		for i in range(x+1,8):
			if not matrix[y][i].isupper():
				moves.append((i,y))
			else:
				break
	#for black rook
	elif matrix[y][x] == 'r' and player == 'black':
		for j in range(y-1,-1,-1):
			if not matrix[j][x].islower():
				moves.append((x,j))
			else:
				break
		for j in range(y+1,8):
			if not matrix[j][x].islower():
				moves.append((x,j))
			else:
				break
		for i in range(x-1,-1,-1):
			if not matrix[y][i].islower():
				moves.append((i,y))
			else:
				break
		for i in range(x+1,8):
			if not matrix[y][i].islower():
				moves.append((i,y))
			else:
				break
	#for white knight (one case for each diagonal)
	elif matrix[y][x] == 'N' and player == 'white':
		if (x-1) >= 0 and (y-2) >= 0:
			if not matrix[y-2][x-1].isupper():
				moves.append((x-1,y-2))

		if (x-2) >= 0 and (y-1) >= 0:
			if not matrix[y-1][x-2].isupper():
				moves.append((x-2,y-1))

		if (x+1) < 8  and (y-2) >= 0:
			if not matrix[y-2][x+1].isupper():
				moves.append((x+1,y-2))

		if (x+2) < 8 and (y-1) >= 0:
			if not matrix[y-1][x+2].isupper():
				moves.append((x+2,y-1))

		if (x-1) >= 0 and (y+2) < 8:
			if not matrix[y+2][x-1].isupper():
				moves.append((x-1,y+2))

		if (x-2) >= 0 and (y+1) < 8:
			if not matrix[y+1][x-2].isupper():
				moves.append((x-2,y+1))

		if (x+1) < 8  and (y+2)  < 8:
			if not matrix[y+2][x+1].isupper():
				moves.append((x+1,y+2))

		if (x+2) < 8 and (y+1)  < 8:
			if not matrix[y+1][x+2].isupper():
				moves.append((x+2,y+1))
	#for black knight
	elif matrix[y][x] == 'n' and player == 'black':
		if (x-1) >= 0 and (y-2) >= 0:
			if not matrix[y-2][x-1].islower():
				moves.append((x-1,y-2))

		if (x-2) >= 0 and (y-1) >= 0:
			if not matrix[y-1][x-2].islower():
				moves.append((x-2,y-1))

		if (x+1) < 8  and (y-2) >= 0:
			if not matrix[y-2][x+1].islower():
				moves.append((x+1,y-2))

		if (x+2) < 8 and (y-1) >= 0:
			if not matrix[y-1][x+2].islower():
				moves.append((x+2,y-1))

		if (x-1) >= 0 and (y+2) < 8:
			if not matrix[y+2][x-1].islower():
				moves.append((x-1,y+2))

		if (x-2) >= 0 and (y+1) < 8:
			if not matrix[y+1][x-2].islower():
				moves.append((x-2,y+1))

		if (x+1) < 8  and (y+2)  < 8:
			if not matrix[y+2][x+1].islower():
				moves.append((x+1,y+2))

		if (x+2) < 8 and (y+1)  < 8:
			if not matrix[y+1][x+2].islower():
				moves.append((x+2,y+1))
	#for white bishop
	elif matrix[y][x] == 'B' and player == 'white':
		for i in range(1,8): #up and left diagonal
			if (x-i) >= 0 and (y-i) >=0:
				if not matrix[y-i][x-i].isupper():
					moves.append((x-i,y-i))
				else:
					break
			else:
				break
		for i in range(1,8): #up and right diagonal
			if (x+i) <= 7 and (y-i) >=0:
				if not matrix[y-i][x+i].isupper():
					moves.append((x+i,y-i))
				else:
					break
			else:
				break
		for i in range(1,8): #down and left diagonal
			if (x-i) >= 0 and (y+i) <=7:
				if not matrix[y+i][x-i].isupper():
					moves.append((x-i,y+i))
				else:
					break
			else:
				break
		for i in range(1,8): #down and right diagonal
			if (x+i) <= 7 and (y+i) <= 7:
				if not matrix[y+i][x+i].isupper():
					moves.append((x+i,y+i))
				else:
					break
			else:
				break
	#for black bishop
	elif matrix[y][x] == 'b' and player == 'black':
		for i in range(1,8): #up and left diagonal
			if (x-i) >= 0 and (y-i) >=0:
				if not matrix[y-i][x-i].islower():
					moves.append((x-i,y-i))
				else:
					break
			else:
				break
		for i in range(1,8): #up and right diagonal
			if (x+i) <= 7 and (y-i) >=0:
				if not matrix[y-i][x+i].islower():
					moves.append((x+i,y-i))
				else:
					break
			else:
				break
		for i in range(1,8): #down and left diagonal
			if (x-i) >= 0 and (y+i) <=7:
				if not matrix[y+i][x-i].islower():
					moves.append((x-i,y+i))
				else:
					break
			else:
				break
		for i in range(1,8): #down and right diagonal
			if (x+i) <= 7 and (y+i) <= 7:
				if not matrix[y+i][x+i].islower():
					moves.append((x+i,y+i))
				else:
					break
			else:
				break

	#for white queen
	elif matrix[y][x] == 'Q' and player == 'white':
		for j in range(y-1,-1,-1):#attacking up
			if not matrix[j][x].isupper():
				moves.append((x,j))
			else:
				break
		for j in range(y+1,8): #attacking down
			if not matrix[j][x].isupper():
				moves.append((x,j))
			else:
				break
		for i in range(x-1,-1,-1): #left
			if not matrix[y][i].isupper():
				moves.append((i,y))
			else:
				break
		for i in range(x+1,8): #right
			if not matrix[y][i].isupper():
				moves.append((i,y))
			else:
				break
		for i in range(1,8): #up and left diagonal
			if (x-i) >= 0 and (y-i) >=0:
				if not matrix[y-i][x-i].isupper():
					moves.append((x-i,y-i))
				else:
					break
			else:
				break
		for i in range(1,8): #up and right diagonal
			if (x+i) <= 7 and (y-i) >=0:
				if not matrix[y-i][x+i].isupper():
					moves.append((x+i,y-i))
				else:
					break
			else:
				break
		for i in range(1,8): #down and left diagonal
			if (x-i) >= 0 and (y+i) <=7:
				if not matrix[y+i][x-i].isupper():
					moves.append((x-i,y+i))
				else:
					break
			else:
				break
		for i in range(1,8): #down and right diagonal
			if (x+i) <= 7 and (y+i) <= 7:
				if not matrix[y+i][x+i].isupper():
					moves.append((x+i,y+i))
				else:
					break
			else:
				break
	#for black queen
	elif matrix[y][x] == 'q' and player == 'black':
		for j in range(y-1,-1,-1):#attacking up
			if not matrix[j][x].islower():
				moves.append((x,j))
			else:
				break
		for j in range(y+1,8): #attacking down
			if not matrix[j][x].islower():
				moves.append((x,j))
			else:
				break
		for i in range(x-1,-1,-1): #left
			if not matrix[y][i].islower():
				moves.append((i,y))
			else:
				break
		for i in range(x+1,8): #right
			if not matrix[y][i].islower():
				moves.append((i,y))
			else:
				break
		for i in range(1,8): #up and left diagonal
			if (x-i) >= 0 and (y-i) >=0:
				if not matrix[y-i][x-i].islower():
					moves.append((x-i,y-i))
				else:
					break
			else:
				break
		for i in range(1,8): #up and right diagonal
			if (x+i) <= 7 and (y-i) >=0:
				if not matrix[y-i][x+i].islower():
					moves.append((x+i,y-i))
				else:
					break
			else:
				break
		for i in range(1,8): #down and left diagonal
			if (x-i) >= 0 and (y+i) <=7:
				if not matrix[y+i][x-i].islower():
					moves.append((x-i,y+i))
				else:
					break
			else:
				break
		for i in range(1,8): #down and right diagonal
			if (x+i) <= 7 and (y+i) <= 7:
				if not matrix[y+i][x+i].islower():
					moves.append((x+i,y+i))
				else:
					break
			else:
				break


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

	new_State = State(currentState,temp_matrix,currentState.nextTurn(),(currentState.getDepth() +1 ) )

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
	#print("running alpha max")
	bestState = None
	if depth == 4:
		return (evalFunction(currentState),bestState)
	for piece in explore1(currentState):
		for possibleMove in validMoves(currentState,piece):
			nextState = move(currentState,piece,possibleMove)
			score = alpha_beta_min(nextState, alpha, beta, depth + 1)[0]
			#nextState.display()
			if bestState == None:
				bestState = nextState

			if score >= beta:
				return (score,nextState) #beta-cutoff
			if score > alpha:
				bestState = nextState
				alpha = score #alpha keeps the maximum value from child
			# print("depth: "+ str(depth))
			# print("alpha: "+ str(alpha))
			# print("beta: "+ str(beta))
	return (alpha,bestState)



def alpha_beta_min(currentState, alpha, beta, depth):
	#print("running alpha min")
	bestState = None
	if depth == 4:
		return (evalFunction(currentState),bestState)
	for piece in explore1(currentState):
		for possibleMove in validMoves(currentState,piece):
			nextState = move(currentState,piece,possibleMove)
			score = alpha_beta_max(nextState,alpha,beta, depth+1)[0]
			#nextState.display()
			if bestState == None:
				bestState = nextState

			if score <= alpha:
				return (score,nextState)
			if score < beta:
				bestState = nextState
				beta = score	
			#print("depth: "+ str(depth))
			#print("alpha: "+ str(alpha))
			#print("beta: "+ str(beta))
	return (beta,bestState)


def runGame(matrix):
		#deep copy
		#call move methods based on piece
		#get deep copy returned 
		#add to list of successors
		#once all successor states reached 
		#return list of successors. 
	currentState = State(None,matrix,'white',0)
	while currentState.getDepth()<5:
		currentState.display()

		#if either player wins, print a statement and quit 
		if(checkmate('white')):
			print('black player wins!')	
			return
		elif(checkmate('black')):
			print('white player wins!')
			return

		if currentState.getTurn() == 'white':
			(score,currentState) = alpha_beta_max(currentState,-10000000, 10000000,0)
			print(score)
			
			#add code for AI
		else:
			(score,currentState) = alpha_beta_min(currentState,-10000000, 10000000,0)
			print(score)
			
			#add code for user input and checks for validation
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





InitialState = State(None,initialB,'white',0)
InitialState.display()
print("white pieces are on: ", end = ' ')
print(explore1(InitialState))

print(validMoves(InitialState,(5,7)))
runGame(initialA)
#print("Initial State B")
#display(initialB)
#print("")
#print("Initial State C")
#display(initialC)
#print("")
