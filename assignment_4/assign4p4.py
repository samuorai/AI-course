# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9  2025
assignment #4 program #4

@author: Wael Badr

Write a program to print a triangle pattern using nested for loops (e.g., 
1
22
333).

"""

import time

print("************************************************************")
print("************* triangle pattern using nested loop ***********")
print("************************************************************")

time.sleep(1)
rows = int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for j in range(i):
        print(i,end='') # to make the row end when it is empty 
    print() # to make a new line after each row