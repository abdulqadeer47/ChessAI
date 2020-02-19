import copy
import math
import random
from state import*


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

	#add time component
	function_sum += currentState.getDepth() * -0.01
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
		if y == 6:
			moves.append((x,y-1))
			moves.append((x,y-2))

		elif (y > 0):
			if matrix[y-1][x] == '_': #move straight
				moves.append(tuple([x,y-1]))
			if (x >0):
				if matrix[y-1][x-1] != '_' and matrix[y-1][x-1].islower(): #attack left
					moves.append(tuple([x-1,y-1]))
			if (x<7):
				if matrix[y-1][x+1] != '_' and matrix[y-1][x+1].islower(): #attack right
					moves.append(tuple([x+1,y-1]))

	elif matrix[y][x] == 'p' and player == 'black':
		if y == 1:
			moves.append((x,y+1))
			moves.append((x,y+2))
		elif (y < 7):
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
				if matrix[j][x].islower():
					break
			else:
				break
		for j in range(y+1,8):
			if not matrix[j][x].isupper():
				moves.append((x,j))
				if matrix[j][x].islower():
					break
			else:
				break
		for i in range(x-1,-1,-1):
			if not matrix[y][i].isupper():
				moves.append((i,y))
				if matrix[y][i].islower():
					break
			else:
				break
		for i in range(x+1,8):
			if not matrix[y][i].isupper():
				moves.append((i,y))
				if matrix[y][i].islower():
					break
			else:
				break
	#for black rook
	elif matrix[y][x] == 'r' and player == 'black':
		for j in range(y-1,-1,-1): #up
			if not matrix[j][x].islower():
				moves.append((x,j))
				if matrix[j][x].isupper():
					break
			else:
				break
		for j in range(y+1,8): #down
			if not matrix[j][x].islower():
				moves.append((x,j))
				if matrix[j][x].isupper():
					break
			else:
				break
		for i in range(x-1,-1,-1): #left
			if not matrix[y][i].islower():
				moves.append((i,y))
				if matrix[y][i].isupper():
					break
			else:
				break
		for i in range(x+1,8): #right
			if not matrix[y][i].islower():
				moves.append((i,y))
				if matrix[y][i].isupper():
					break
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
					if matrix[y-i][x-i].islower():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #up and right diagonal
			if (x+i) <= 7 and (y-i) >=0:
				if not matrix[y-i][x+i].isupper():
					moves.append((x+i,y-i))
					if matrix[y-i][x+i].islower():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #down and left diagonal
			if (x-i) >= 0 and (y+i) <=7:
				if not matrix[y+i][x-i].isupper():
					moves.append((x-i,y+i))
					if matrix[y+i][x-i].islower():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #down and right diagonal
			if (x+i) <= 7 and (y+i) <= 7:
				if not matrix[y+i][x+i].isupper():
					moves.append((x+i,y+i))
					if matrix[y+i][x+i].islower():
						break
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
					if matrix[y-i][x-i].isupper():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #up and right diagonal
			if (x+i) <= 7 and (y-i) >=0:
				if not matrix[y-i][x+i].islower():
					moves.append((x+i,y-i))
					if matrix[y-i][x+i].isupper():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #down and left diagonal
			if (x-i) >= 0 and (y+i) <=7:
				if not matrix[y+i][x-i].islower():
					moves.append((x-i,y+i))
					if matrix[y+i][x-i].isupper():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #down and right diagonal
			if (x+i) <= 7 and (y+i) <= 7:
				if not matrix[y+i][x+i].islower():
					moves.append((x+i,y+i))
					if matrix[y+i][x+i].isupper():
						break
				else:
					break
			else:
				break

	#for white queen
	elif matrix[y][x] == 'Q' and player == 'white':
		for j in range(y-1,-1,-1): #up
			if not matrix[j][x].isupper():
				moves.append((x,j))
				if matrix[j][x].islower():
					break
			else:
				break
		for j in range(y+1,8): #down
			if not matrix[j][x].isupper():
				moves.append((x,j))
				if matrix[j][x].islower():
					break
			else:
				break
		for i in range(x-1,-1,-1): #left
			if not matrix[y][i].isupper():
				moves.append((i,y))
				if matrix[y][i].islower():
					break
			else:
				break
		for i in range(x+1,8): #right
			if not matrix[y][i].isupper():
				moves.append((i,y))
				if matrix[y][i].islower():
					break
			else:
				break

		for i in range(1,8): #up and left diagonal
			if (x-i) >= 0 and (y-i) >=0:
				if not matrix[y-i][x-i].isupper():
					moves.append((x-i,y-i))
					if matrix[y-i][x-i].islower():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #up and right diagonal
			if (x+i) <= 7 and (y-i) >=0:
				if not matrix[y-i][x+i].isupper():
					moves.append((x+i,y-i))
					if matrix[y-i][x+i].islower():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #down and left diagonal
			if (x-i) >= 0 and (y+i) <=7:
				if not matrix[y+i][x-i].isupper():
					moves.append((x-i,y+i))
					if matrix[y+i][x-i].islower():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #down and right diagonal
			if (x+i) <= 7 and (y+i) <= 7:
				if not matrix[y+i][x+i].isupper():
					moves.append((x+i,y+i))
					if matrix[y+i][x+i].islower():
						break
				else:
					break
			else:
				break


	#for black queen
	elif matrix[y][x] == 'q' and player == 'black':
		for j in range(y-1,-1,-1): #up
			if not matrix[j][x].islower():
				moves.append((x,j))
				if matrix[j][x].isupper():
					break
			else:
				break
		for j in range(y+1,8): #down
			if not matrix[j][x].islower():
				moves.append((x,j))
				if matrix[j][x].isupper():
					break
			else:
				break
		for i in range(x-1,-1,-1): #left
			if not matrix[y][i].islower():
				moves.append((i,y))
				if matrix[y][i].isupper():
					break
			else:
				break
		for i in range(x+1,8): #right
			if not matrix[y][i].islower():
				moves.append((i,y))
				if matrix[y][i].isupper():
					break
			else:
				break
		for i in range(1,8): #up and left diagonal
			if (x-i) >= 0 and (y-i) >=0:
				if not matrix[y-i][x-i].islower():
					moves.append((x-i,y-i))
					if matrix[y-i][x-i].isupper():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #up and right diagonal
			if (x+i) <= 7 and (y-i) >=0:
				if not matrix[y-i][x+i].islower():
					moves.append((x+i,y-i))
					if matrix[y-i][x+i].isupper():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #down and left diagonal
			if (x-i) >= 0 and (y+i) <=7:
				if not matrix[y+i][x-i].islower():
					moves.append((x-i,y+i))
					if matrix[y+i][x-i].isupper():
						break
				else:
					break
			else:
				break
		for i in range(1,8): #down and right diagonal
			if (x+i) <= 7 and (y+i) <= 7:
				if not matrix[y+i][x+i].islower():
					moves.append((x+i,y+i))
					if matrix[y+i][x+i].isupper():
						break
				else:
					break
			else:
				break
	

	#add more for each piece. 
	#Note: it will be the same for both white and black for pieces other than the pawn.
	return moves

#takes in a tuple, sorts by distance
def sortValidMoves(positions, posFrom):
	distance = []
	newpositions = []
	for pos in positions:
		d = math.sqrt((posFrom[0]-pos[0])**2 + (posFrom[1]-pos[1])**2)
		distance.append((d,pos[0],pos[1]))
	
	distance.sort()
	for item in distance:
		newpositions.append((item[1],item[2]))

	return newpositions


#moves the piece and updates state accordingly
def move(currentState, posFrom, posTo):
	x = posFrom[0]
	y = posFrom[1]

	temp_matrix = copy.deepcopy(currentState.getMatrix())

	temp_matrix[posTo[1]][posTo[0]] = temp_matrix[y][x]
	temp_matrix[y][x] = '_'

	new_State = State(currentState,temp_matrix,currentState.nextTurn(),(currentState.getDepth() +1 ) )

	return new_State

#Exploration policy 1
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

#Exploration policy 2
def explore2(currentState):
	#returns a list of tuples with x,y coordinates of all the pieces based on importance
	#the order is: king, queen, rook, knight, bishop, pawn.
	pieces = explore1(currentState)
	newpieces = []
	matrix = currentState.getMatrix()

	for piece in pieces:
		if matrix[piece[1]][piece[0]] == 'K' or matrix[piece[1]][piece[0]] == 'k':
			newpieces.append(piece)
	for piece in pieces:
		if matrix[piece[1]][piece[0]] == 'Q' or matrix[piece[1]][piece[0]] == 'q':
			newpieces.append(piece)
	for piece in pieces:
		if matrix[piece[1]][piece[0]] == 'R' or matrix[piece[1]][piece[0]] == 'r':
			newpieces.append(piece)
	for piece in pieces:
		if matrix[piece[1]][piece[0]] == 'N' or matrix[piece[1]][piece[0]] == 'n':
			newpieces.append(piece)
	for piece in pieces:
		if matrix[piece[1]][piece[0]] == 'B' or matrix[piece[1]][piece[0]] == 'b':
			newpieces.append(piece)
	for piece in pieces:
		if matrix[piece[1]][piece[0]] == 'P' or matrix[piece[1]][piece[0]] == 'p':
			newpieces.append(piece)

	return newpieces

def alpha_beta_max(currentState, alpha, beta, depth,exploreMethod):
	nodesExplored = 0
	#print("running alpha max")
	bestState = None
	if depth == 4:
		return (evalFunction(currentState),bestState,1)
	if exploreMethod == 1:
		pieces = explore1(currentState)
		random.shuffle(pieces)
	else:
		pieces = explore2(currentState)

	for piece in pieces:
		moves = validMoves(currentState,piece)
		if exploreMethod == 1:
			random.shuffle(moves)
		else:
			moves = sortValidMoves(moves, piece)

		for possibleMove in moves:
			nextState = move(currentState,piece,possibleMove)
			(score,x,morenodes) = alpha_beta_min(nextState, alpha, beta, depth + 1,exploreMethod)
			nodesExplored +=morenodes
			#nextState.display()
			if bestState == None:
				bestState = nextState
			if score >= beta:
				return (score,nextState,nodesExplored) #beta-cutoff
			if score > alpha:
				bestState = nextState
				alpha = score #alpha keeps the maximum value from child
			# print("depth: "+ str(depth))
			# print("alpha: "+ str(alpha))
			# print("beta: "+ str(beta))
	return (alpha,bestState,nodesExplored)



def alpha_beta_min(currentState, alpha, beta, depth,exploreMethod):
	nodesExplored = 0
	#print("running alpha min")
	bestState = None
	if depth == 4:
		return (evalFunction(currentState),bestState,1)
	if exploreMethod == 1:
		pieces = explore1(currentState)
		random.shuffle(pieces)
	else:
		pieces = explore2(currentState)

	for piece in pieces:
		moves = validMoves(currentState,piece)
		if exploreMethod == 1:
			random.shuffle(moves)
		else:
			moves = sortValidMoves(moves, piece)

		for possibleMove in moves:
			nextState = move(currentState,piece,possibleMove)
			(score,x,morenodes) = alpha_beta_max(nextState,alpha,beta, depth+1,exploreMethod)
			#nextState.display()
			nodesExplored +=morenodes

			if bestState == None:
				bestState = nextState

			if score <= alpha:
				return (score,nextState,nodesExplored)
			if score < beta:
				bestState = nextState
				beta = score	
			#print("depth: "+ str(depth))
			#print("alpha: "+ str(alpha))
			#print("beta: "+ str(beta))
	return (beta,bestState,nodesExplored)

#Main method that runs with both players simulated by the AI
def runGame(matrix, exploreMethod):
	currentState = State(None,matrix,'white',0)
	while currentState.getDepth()<5:
		currentState.display()

		#if either player wins, print a statement and quit 
		if endgame(currentState):
			print("The game has ended")
			return

		if currentState.getTurn() == 'white':
			(score,currentState,nodesExplored) = alpha_beta_max(currentState,-10000000, 10000000,0,exploreMethod)
			print('nodes explored: '+str(nodesExplored) )
			print('score: ' + str(score))			
			#add code for AI
		else:
			(score,currentState,nodesExplored) = alpha_beta_min(currentState,-10000000, 10000000,0,exploreMethod)
			print('nodes explored: '+str(nodesExplored) )
			print('score: ' + str(score))

#Main method that runs with white player simulated by the AI
def runGameUser(matrix,exploreMethod):
	currentState = State(None,matrix,'white',0)
	finish = False
	while finish == False:
		currentState.display()

		#if either player wins, print a statement and quit 
		if endgame(currentState):
			print("The game has ended")
			return

		if currentState.getTurn() == 'black':
			(score,currentState,nodesExplored) = alpha_beta_min(currentState,-10000000, 10000000,0,exploreMethod)
			print('nodes explored: '+str(nodesExplored) )
			print('score: ' + str(score))			
			#add code for AI
		else:
			validEntry = False
			while validEntry == False:
				print('Your turn (White Player)')
				print('enter starting position and end position (example:\'a2 a3\'')
				user = input()
				if user == 'finish':
					finish = True
					break
				posFrom = (ord(user[0])-97,8-int(user[1]))
				posTo = (ord(user[3])-97,8-int(user[4]))

				possibleMoves = validMoves(currentState,posFrom)
				if posTo in possibleMoves:
					validEntry = True
					currentState = move(currentState,posFrom,posTo)
				else:
					print('please enter a valid move!')
	print("The game has ended")


#look for checkmate of the player's king. Will make use of valid moves function for opponent pieces
def endgame(currentState):
	whiteWin = True
	blackWin = True
	matrix = currentState.getMatrix()
	for row in matrix:
		for value in row:
			if value == 'K':
				blackWin = False
			if value == 'k':
				whiteWin = False
	
	if whiteWin == True:
		print('The White Player has won!')
	if blackWin == True:
		print('The Black Player has won!')

	return (whiteWin or blackWin)

