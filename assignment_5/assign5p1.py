# -*- coding: utf-8 -*-
"""
Created on Sun Nov  18  2025
assignment #5 program #1

@author: Wael Badr

Create 4 types of user defined function that add two numbers.
"""
# Type 1 --> takes parameters and return value.

def type1(num1,num2):
        return num1+num2
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("num1 + num1 = ",type1(num1,num2))

#%%
#type 2 --> takes parameters and return no value.

def type2(num1,num2):
    total = num1+num2
    print("num1 + num1 = ",total)
    
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

type2(num1,num2)
#%%

#type 3 --> doesn't take parameters and return value.

def type3():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    total = num1+num2
    return total
    
print("num1 + num1 = ",type3())
#%%

#type 4 --> doesn't take parameters and return no value.

def type4():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    total = num1+num2
    print("num1 + num1 = ",total)
    
type4()