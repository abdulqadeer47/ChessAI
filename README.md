# ChessAI
This AI makes use of H-MiniMax to determine the next move. Alpha-Beta pruning is used to reduce computational time and improve efficiency. After testing the AI over different board configurations, it was found that the AI makes only valid and makes “smart” moves to increase chances of winning i.e. to capture the king. 

To run the program:

1) Save all three files in a known folder on a computer. 

2) Run lab2.py from the command line using: python3 lab2.py

3) And press enter/return.

This will run the three initial states for the next 5 moves with the first evaluation function. Then you play as the white player, with the black player being simulated by the AI.

********************  Modifications *********************
Upon starting the program asks for exploration method to be selected. There are two options

Exploration Policy 1: a random shuffle in both pieces and possible moves for each piece
Exploration Policy 2: sorted by most important piece that can move first, then by distance of each possible move.

Press 1 and then hit enter to run AI with Exploration Policy 1. 
or
Press 2 and then hit enter to run AI with Exploration Policy 2. 


To move a piece on the board while playing with the AI, enter the cell number of the piece you want to move, (for e.g. a2) followed by a space (' '), followed by the grid number of the cell you want to move the piece to (for e.g. a3). 
(a2 a3) moves a piece from a2 to a3. 
