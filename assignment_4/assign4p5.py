# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9  2025
assignment #4 program #5

@author: Wael Badr

Write a program to simulate a simple guessing game: guess a number 1-10, 
continue until correct or "quit" to break.

"""

import time

print("************************************************************")
print("********************* number guessing **********************")
print("************************************************************")

time.sleep(1)
hidden_num = 4
while 1:
    num = int(input("Guess a number from 1 - 10: "))
   
    if num == hidden_num:
        print("correct!")
        break
    else:
       state = input("not lucky, try again?(y / n)")
    if state == 'y':
        continue
    else:
        print("game ended")
        break