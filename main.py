# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:19:59 2019

@author: muin
"""

from AlphaBeta import *
from BoardLogic import *
from Heuristics import *

alpha = float('-inf')
beta = float('inf')
depth = 5

def printBoard(board):
        print("")
        print(board[0]+"(00)----------------------"+board[1]+"(01)--------------------"+board[2]+"(02)");
        print("|                           |                           |");
        print("|       "+board[8]+"(08)--------------"+board[9]+"(09)--------------"+board[10]+"(10)     |");
        print("|       |                   |                    |      |");
        print("|       |                   |                    |      |");
        print("|       |        "+board[16]+"(16)-----"+board[17]+"(17)-----"+board[18]+"(18)       |      |");
        print("|       |         |                   |          |      |");
        print("|       |         |                   |          |      |");
        print(board[3]+"(03)---"+board[11]+"(11)----"+board[19]+"(19)               "+board[20]+"(20)----"+board[12]+"(12)---"+board[4]+"(04)");
        print("|       |         |                   |          |      |");
        print("|       |         |                   |          |      |");
        print("|       |        "+board[21]+"(21)-----"+board[22]+"(22)-----"+board[23]+"(23)       |      |");
        print("|       |                   |                    |      |");
        print("|       |                   |                    |      |");
        print("|       "+board[13]+"(13)--------------"+board[14]+"(14)--------------"+board[15]+"(15)     |");
        print("|                           |                           |");
        print("|                           |                           |");
        print(board[5]+"(05)----------------------"+board[6]+"(06)--------------------"+board[7]+"(07)");
        print("#########################################################")
    
def HUMAN_VS_AI(heuristic_stage1, heuristic_stage23):
    
    board = []
    for i in range(24):
        board.append("X")
    
    #Calls evaluator class from AlphaBeta.py    
    evaluation = evaluator()
    
    print("Player 1 = Human")
    print("Player 2 = AI")
    for i in range(9):

        printBoard(board)
        finished = False
        while not finished:
            try:

                pos = int(input("Place '1' piece: "))    
                
                if board[pos] == "X":
                    
                    board[pos] = '1'
                    if isCloseMill(pos, board):
                        itemPlaced = False
                        while not itemPlaced:
                            try:

                                pos = int(input("Remove '2' piece: "))
                                
                                if board[pos] == "2" and not isCloseMill(pos, board) or (isCloseMill(pos, board) and getNumberOfPieces(board, "1") == 3):
                                    board[pos] = "X"
                                    itemPlaced = True
                                else:
                                    print("Invalid position")
                                    
                            except Exception:
                                print("You can not remove it\n Try another piece.")

                    finished = True

                else:
                    print("There is already a piece there")

            except Exception:
                print("Couldn't get the input value")
        
        printBoard(board)
        evalBoard = alphaBetaPruning(board, depth, False, alpha, beta, True, heuristic_stage1)

        if evalBoard.evaluator == float('-inf'):
            print("")
            print("Game Over!")
            print("You Lost :(")
            return 0
        else:
            board = evalBoard.board

    endStagesFinished = False
    while not endStagesFinished:

        printBoard(board)
        
        #Get the users next move
        userHasMoved = False
        while not userHasMoved:
            try:
                pos = int(input("Move '1' piece: "))

                while board[pos] != '1':
                    pos = int(input("Move '1' piece: ")) 

                userHasPlaced = False
                while not userHasPlaced:

                    newPos = int(input("New position for '1': "))

                    if board[newPos] == "X":
                        board[pos] = 'X'
                        board[newPos] = '1'

                        if isCloseMill(newPos, board):
                            
                            userHasRemoved = False
                            while not userHasRemoved:
                                try:

                                    pos = int(input("Remove '2' piece: "))
                                    
                                    if board[pos] == "2" and not isCloseMill(pos, board) or (isCloseMill(pos, board) and getNumberOfPieces(board, "1") == 3):
                                        board[pos] = "X"
                                        userHasRemoved = True
                                    else:
                                        print("Invalid position")
                                except Exception:
                                    print("Piece is in a Closed Mill")

                        userHasPlaced = True
                        userHasMoved = True

                    else:
                        print("You cannot move there")

            except Exception:
                print("You cannot move there")

        if getEvaluationStage23(board) == float('inf'):
            print("")
            print("Congratulations!")
            print("You Won!")
            return 0

        printBoard(board)

        evaluation = alphaBetaPruning(board, depth, False, alpha, beta, False, heuristic_stage23)

        if evaluation.evaluator == float('-inf'):
            print("")
            print("Game Over")
            print("You Lost :(")
            return 0
        else:
            board = evaluation.board


if __name__ == "__main__":
    
    print("Welcome to Nine Mens Morris")
    print("****************************")
    HUMAN_VS_AI(numberOfPiecesHeuristic, AdvancedHeuristic)
