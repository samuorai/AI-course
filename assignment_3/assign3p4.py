# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:06:36 2025
assignment #3 program #4

@author: Wael Badr

Write a program that takes a
number as input and uses relational and logical operators to check the following
conditions. Print True or False for each with a descriptive message.
"""

import time

print("************************************************************")
print("************ Relational and Logical Operators **************")
print("************************************************************")

time.sleep(1)
while 1:
    try:
        num = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
    else:
        if num >= 1 and num <= 10:
            print("number between 1 and 10: True")
        else:
            print("number between 1 and 10: False")
        if num % 2 == 0:
            even = True
        else:
            even = False
        if num > 0:
            positive = True
        else:
            positive = False
        print("number is even: ",even,", number is positive: ", positive)
        if num != 0:
            Not_equal = True
        else:
            Not_equal = False
        if num > 100:
                greater = True
        else:
                greater = False
        print("number not equal to Zero:",Not_equal, ", number grater than 100: ",greater)
    finally:
        state = input("would you like to try another number? (y / n)")
        if state.lower() == 'y':
            continue
        elif state.lower() == 'n':
            print("program complete")
            break
        else:
            break