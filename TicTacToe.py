#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:50:59 2020

@author: diana
"""
import random

def insertLetter(letter, pos):
    if board[pos] == " ":
        board[pos]=letter
        return True
    else: 
        return False 
    
    
def printBoard(board):
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("-----------")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("-----------")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")    
    
    
def isBoardFull(board):
    if list(board.values()).count(" ") > 0: 
        return False
    else:
        return True
    
    
def isWinner(b):
    for n in [1, 4, 7]:
        if not(b[n] == " ") and b[n] == b[n+1] == b[n+2]:
            return b[n];
    for n in range(1,4):
        if not(b[n] == " ") and b[n] == b[n+3] == b[n+6]:
            return b[n];
    if not(b[5] == " ") and ((b[1] == b[5] == b[9]) or (b[3] == b[5] == b[7])):
        return b[5];
    return ""


def playerMove(letter):
    run = True;
    while (run):
        move = input("Please select a position to enter "+letter+": ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if insertLetter(letter, move): 
                    run = False
                else:
                    print("Sorry, this space is occupied")
            else:
                print("The position must be between 1 and 9")
        except:
            print("Please enter a valid number")
    
    
           
def computerMove():
    possibleMoves = [pos for pos in board if board[pos] == " "]
    for letter in players:
        for pos in possibleMoves:
            boardCopy = board.copy()
            boardCopy[pos] = letter
            if isWinner(boardCopy) == letter:
                return pos
     
    if 5 in possibleMoves:
        return 5
          
    cornersOpen = []
    for pos in possibleMoves:
        if pos in [1, 3, 7, 9]:
            cornersOpen.append(pos)
    
    if len(cornersOpen) > 0:
        return random.choice(cornersOpen)
    
    
    edgesOpen = []
    for pos in possibleMoves:
        if pos in [2, 4, 6, 8]:
            edgesOpen.append(pos)
            
    if len(edgesOpen) > 0:
        return random.choice(edgesOpen)
            
def decideSymbol():
    user = ""
    pc = ""
    while user == "":
        attempt = input("Choose your symbol (only 1 character): ")
        if len(attempt) == 1:
            user = attempt
            if user == "O":
                pc = "X"
            else:
                pc = "O"
        return [pc, user]
   
    
print("Welcome to Tic Tac Toe!")
board = {x:" " for x in range(1,10)}
players = decideSymbol()
printBoard(board)
while isWinner(board) == "" and isBoardFull(board) == False:
    playerMove(players[1])
    if isWinner(board) == players[1]:
        printBoard(board)
        print("\nCongratulations! You win")
    else:
        board[computerMove()] = players[0]
        printBoard(board)
        if isWinner(board) == players[0]:
            print("\nYou loose... Are you letting AI dominate??")
else: 
    if isWinner(board) == "" and isBoardFull(board):
        print("\nEOG. You both win!")