# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:06:36 2025
assignment #3 program #6

@author: Wael Badr

Write a program that takes a persons
age as input and uses an if-else statement to check if they are eligible to
vote (age ≥ 18). Print "You are eligible to vote." or "You are not eligible
to vote." Use try-except for invalid inputs and ensure correct indentation.
"""

import time

print("************************************************************")
print("***************  if-else Voting Eligibility ****************")
print("************************************************************")

time.sleep(1)
while 1:
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid input!")
    else:
        if age <=0:
            print("that is not an age!")
        elif age >= 18 and age <=70:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    finally:
        state = input("would you lke to try again? (y / n)")
        if state.lower() == 'y':
            continue
        elif state.lower() == 'n':
            print("program complete")
            break
        else:
            break