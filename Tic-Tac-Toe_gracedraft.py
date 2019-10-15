#HELP: 
# 1)how to while loop for position not in range(1,9)
# 2)recheck computer strategy


import os
import time
import random

def show_header():
	"""

"TIC-TAC-TOE"

1 | 2 | 3
4 | 5 | 6
7 | 8 | 9

Choose a position from 1 to 9.
The first one to get three in a row wins the game. Good luck!

"""

board = [" ", " ", " ",
		 " ", " ", " ",
		 " ", " ", " "]

def show_board():
	print (board[0] + " | " + board[1] + " | " + board[2])
	print (board[3] + " | " + board[4] + " | " + board[5])
	print (board[6] + " | " + board[7] + " | " + board[8])

	
def winner(board, player):
	if board[0]==player and board[1]==player and board[2]==player or \
		board[3]==player and board[4]==player and board[5]==player or \
		board[6]==player and board[7]==player and board[8]==player or \
		board[0]==player and board[3]==player and board[6]==player or \
		board[1]==player and board[4]==player and board[7]==player or \
		board[2]==player and board[5]==player and board[8]==player or \
		board[0]==player and board[4]==player and board[8]==player or \
		board[2]==player and board[4]==player and board[6]==player:
		return True
	return False


def full_board(board):
	if " " in board:
		return False
	return True


def computer_move(board,player):

#computer strategy:
#for columns:
	for i in [0,1,2]:
		if board[i]==" " and board[i+3]==player and board[i+6]==player:
			return i
		elif board[i]==player and board[i+3]==" " and board[i+6]==player:
			return i+3
		elif board[i]==player and board[i+3]==player and board[i+6]==" ":
			return i+6
#for rows:
	for i in [0,3,6]:
		if board[i]==" " and board[i+1]==player and board[i+2]==player:
			return i
		elif board[i]==player and board[i+1]==" " and board[i+2]==player:
			return i+1
		elif board[i]==player and board[i+1]==player and board[i+2]==" ":
			return i+2
# for diagonals:
	for i in [0]:
		if board[i]==" " and board[i+4]==player and board[i+8]==player:
			return i
		elif board[i]==player and board[i+4]==" " and board[i+8]==player:
			return i+4
		elif board[i]==player and board[i+4]==player and board[i+8]==" ":
			return i+8
	for i in [2]:
		if board[i]==" " and board[i+2]==player and board[i+4]==player:
			return i
		elif board[i]==player and board[i+2]==" " and board[i+4]==player:
			return i+2
		elif board[i]==player and board[i+2]==player and board[i+4]==" ":
			return i+4


	while True:
		move=random.randint(1,9)-1
		if board[move]==" ":
			return move
			break


while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print(show_header.__doc__)
	show_board()

#For Player 'X':

	position= int(input("\nPlease choose an empty space for 'X': ")) - 1

	if board[position]==" ":
		board[position]= "X"

	else:
		print("Sorry, the space is not empty.")
		time.sleep(1)

	if winner(board,"X"):
		os.system('cls' if os.name == 'nt' else 'clear')
		print(show_header.__doc__)
		show_board()
		print("\nX wins. Congrats!\n")
		break

	os.system('cls' if os.name == 'nt' else 'clear')
	print(show_header.__doc__)
	show_board()

#For tie:

	if full_board(board):
		print ("It's a tie!")
		break

#For Player 'O':
	
	time.sleep(0.1)
	position=computer_move(board, "O")

	if board[position]==" ":
		board[position]= "O"

	else:
		print("Sorry, the space is not empty.")
		time.sleep(1)

	if winner(board,"O"):
		os.system('cls' if os.name == 'nt' else 'clear')
		print(show_header.__doc__)
		show_board()
		print("\nO wins. Better luck next time!\n")
		break

#For tie:

	if full_board(board):
		print ("It's a tie!")
		break

