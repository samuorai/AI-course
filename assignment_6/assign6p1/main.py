# -*- coding: utf-8 -*-
"""
Created on Sun Nov  24  2025
assignment #6 program #1

@author: Wael Badr

2. In the same project, create another Python file named main.py (outside the 
    custom_Package folder).
    In main.py you must:
        o Import the four functions from Custom_Package.my_functions.
        o Call each function with suitable test values.
        o Print clear output messages showing the result of each function call.
"""

import sys

sys.path.append('D:/python_course/AI-course/assignment_6/assign6p1/Custom_Package')

from Custom_Package.my_functions import add_numbers, factorial, is_even, average
# first function calling:
    
a = float(input("Enter 'a' number: "))
b = float(input("Enter 'b' number: "))
sum = add_numbers(a,b)
print(sum)

print(f"{a:0.2f} + {b:0.2f} = {sum:0.2f}")
#%%
# second function calling:

n = int(input("Enter number to get factorial: "))

print(factorial(n))

#%%
# third function calling:

n = int(input("Enter a number: "))
print(is_even(n))

#%%
#forth function calling:
    
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
avg = average(a,b,c)
print(f"average of {a:0.2f}, {b:0.2f} and {c:0.2f} is: {avg:0.2f}")