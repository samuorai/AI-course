# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9  2025
assignment #4 program #2

@author: Wael Badr

Write a program to calculate factorial of a number using while loop. Handle invalid 
input while.
"""

import time

print("************************************************************")
print("***************** factorial number calculator **************")
print("************************************************************")

time.sleep(1)
while 1:
    try:
        n = int(input("Enter number to get factorial: "))
        count = 1
        fac = 1
    except ValueError:
        print("wrong input, put a number")
    else:
        if n != 0 and n < 0:
            print("Enter a non-negative or not Zero, positive numbers only")
        else:
            while count <= n:
                fac = fac * count
                count = count + 1
        print("factorial of ",n," is ",fac)
    finally:
        state = input("do you want to calculate another number?(y / n) ")
        if state == 'y':
            continue
        else:
            print("thank you")
            break
            
        

