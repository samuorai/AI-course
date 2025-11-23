# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:06:36 2025
assignment #3 program #2

@author: Wael Badr

Write a program that evaluates
the following expressions with different operator precedence and prints the
results with explanations in comments.
"""

import time

print("************************************************************")
print("************ arithmatic operations precedence **************")
print("************************************************************")

time.sleep(1)
while 1:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    z = float(input("Enter third number: "))
    
    situation1 = x + y * z
    situation2 = (x + y) * z
    situation3 = x ** y + z
    situation4 = x / y * z
    situation5 = x % y // z
    
    print(f"Result of {x} + {y} x {z} = {situation1} as {y} x {z} will be performed first, then added to {x} .")
    print(f"Result of ( {x} + {y} ) * {z} = {situation2} as () has precedence to be prformed first, then result multiplied by {z} ")
    print(f"Result of {x} ^ {y} + {z} = {situation3} as the power has precedence to be performed, then result added to {z}")
    print(f"Result of {x} / {y} x {z} = {situation4} as multiplication and division are equal in precedence, so the operation starts from left to right")
    print(f"Result of {x} % {y} // {z} = {situation5} as modulus has highest precedence, then floor division ")
    
    state = input("do you want to try different numbers? (y / n)")
    
    if state.lower() == 'y':
        continue
    elif state.lower() == 'n':
        print("program complete")
        break
    else:
        print(" invalid input, exiting program")
        break