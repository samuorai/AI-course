# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:06:36 2025
assignment #3 program #5

@author: Wael Badr

Write a program that takes a number
as input and uses an if statement to check if it is positive. If true, print "The
number is positive." Ensure proper indentation (4 spaces). Test with positive,
negative, and zero inputs.
"""

import time

print("************************************************************")
print("**************** Simple Branching with if ******************")
print("************************************************************")

time.sleep(1)
while 1:
    try:
        num = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input!")
    else:
        if num > 0:
            pos = True
        else:
            pos = False
        print("number is positive: ",pos)
    finally:
        state = input("would you like to try again (y / n): ")
        if state.lower() == 'y':
            continue
        elif state.lower() == 'n':
            print("program complete")
            break
        else:
            break