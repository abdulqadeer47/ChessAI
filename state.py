class State:
	def __init__(self,par,m,t,d):
		self.parent = par
		self.matrix = m
		self.turn = t
		self.depth = d


	def getParent(self):
		return self.parent

	def getMatrix(self):
		return self.matrix

	def getTurn(self):
		return self.turn

	def getDepth(self):
		return self.depth

	def nextTurn(self):
		if self.turn == 'white':
			return 'black'
		else:
			return 'white'

	def display(self):
		print("player turn: " + self.turn)
		rownum = 8
		for row in self.matrix:
			print(str(rownum)+'|', end ='')
			rownum += -1
			for value in row:
				print(value, end = ' ')
			print("")

		print(' |a b c d e f g h')
