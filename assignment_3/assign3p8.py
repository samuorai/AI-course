# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:06:36 2025
assignment #3 program #8

@author: Wael Badr

Write a sequential program that takes
the length and width of a rectangle as input. Calculate and print the area
(length * width) and perimeter (2 * (length + width)). Use try-except to
handle invalid inputs (e.g., non-numeric values).
"""

import time

print("************************************************************")
print("*************** Rectangle area Calculations ****************")
print("************************************************************")

time.sleep(1)
while 1:
    try:
        width = float(input("Enter width: "))
        length = float(input("Enter length: "))
    except ValueError:
        print("non-numeric values")
    else:
        if width > 0 and length > 0:
            
            Rec_area = width * length
            
            per = 2 * (length + width)
            
            print("rectangle area = ",Rec_area, " and perimeter = ",per)
        else:
            print("Invalid values")
    finally:
        state = input("would you like to try again? (y / n)")
        if state.lower() == 'y':
             continue
        elif state.lower() == 'n':
            print("program complete")
            break
        else:
            break