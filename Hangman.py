#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:42:28 2020

@author: diana
"""
import random    
import re    
    
man = {10:"",9:"  -------  ", 8:"  -------  \n       |", 
       7:"  -------  \n       |\n     0", 
       6:"  -------  \n       |\n     0\n     |",
       5:"  -------  \n       |\n     0\n     |\n    /",
       4:"  -------  \n       |\n     0\n     |\n    / \\", 
       3:"  -------  \n       |\n    \\0\n     |\n    / \\",
       2:"  -------  \n       |\n    \\0/\n     |\n    / \\",
       1:"  -------  \n       |\n    \\0/|\n     |\n    / \\", 
       0:"  -------  \n       |\n     0_|\n    /|\\\n    / \\"}

def hangman(name):
    name = name.title()
    numAttempts = 10
    guessMade = ""
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    word = random.choice(["tiger", "whale", "shark", "horse", "pelican",
             "pokemon", "avengers", "goat", "duck", "rabbit"])
    for i in range(len(word)):
        guessMade += "_ "
    print(guessMade)
    
    while (numAttempts > 0):
        letter = input()
        if len(letter)!=1 or letter not in validLetters:
            print("Input not valid")
            continue
        elif letter in word:
            positions = [i.start() for i in re.finditer(letter, word)]
            for i in positions:
                charGuess = list(guessMade)
                charGuess[i*2]=letter
                guessMade = "".join(charGuess)
            new = guessMade.replace(" ","")
            print(guessMade.upper())
            print(man[numAttempts])
            if new == word:
                print("\nYou win! Congrats "+str(name))
                break
            else:
                continue
        else:
            numAttempts -= 1
            print(guessMade.upper())
            print(man[numAttempts])
            if numAttempts == 0:
                print("\n"+str(name) + " you loooooose :( EOG")
                break
            else:
                print(str.format("{} attempts left", numAttempts))
                continue
            
        

name = input("Enter your name: ")
print("Welcome "+name+"!")
print("-----------------------")
print("Try to get the following word in less than 10 attempts:")
hangman(name)