# -*- coding: utf-8 -*-
"""
Created on Sun Nov  24  2025
assignment #6 program #1

@author: Wael Badr

1. Create a Python package named Custom_Package.
    Inside this package, create a module file called my_functions.py that contains the 
    following four functions:
    1. add_numbers(a, b)
        ▪ Receives two numbers a and b.
        ▪ Returns the sum of the two numbers.
    2. factorial(n)
        ▪ Receives an integer n.
        ▪ Returns the factorial of n (e.g. factorial(5) = 120).
        ▪ Assume n is a non-negative integer.
    3. is_even(n)
        ▪ Receives an integer n.
        ▪ Returns True if n is an even number, otherwise returns False.
    4. average(a, b, c)
        ▪ Receives three numbers a, b, and c.
        ▪ Returns the arithmetic mean (average) of these three numbers.
    
"""
def add_numbers(a,b):
    
    sum = a+b    
    return sum


def factorial(n):
        count = 1
        fac = 1
        if n != 0 and n < 0:
            print("Enter a non-negative or not Zero, positive numbers only")
        else:
            while count <= n:
                fac = fac * count
                count = count + 1
        print("factorial of ",n," is ",fac)
        
def is_even(n):
       
    if n%2 == 0:
        return True
    else:
        return False
            
def average(a,b,c):
    average = (a+b+c)/3
    return average
