***********************  FILES  ************************
There are three files in the package:
	Lab2.py : this is the script that calls the chess game with different initial game setups and evaluation functions

	State.py : the class State is used to create objects of type state that contain the previous state, depth, chess matrix, etc

	Chess.py : this file contains all the methods needed to run the chess game

**********************  RUNNING  ************************
To run the script, run the following line:

	python3 Lab2.py

This will run the three initial states for the next 5 moves with the first evaluation function. Then you play as the white player, with the black player being simulated by the AI.

********************  Modifications *********************
Upon starting the program asks for explore method. There are two options

Method 1: a random shuffle in both pieces and possible moves for each piece
Method 2: sorted by most important piece that can move first, then by distance of each possible move.