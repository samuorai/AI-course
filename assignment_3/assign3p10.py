# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:06:36 2025
assignment #3 program #10

@author: Wael Badr

Write a program that combines sequential
and branching structures. Take the users annual income and number of dependents 
as input. Calculate a tax amount (income * 0.15). Use an if-elif-else
structure to reduce the tax: 20% reduction for 3 or more dependents, 10%
reduction for 1 or 2 dependents, no reduction otherwise. Print the income,
initial tax, reduction, and final tax.
"""

import time

print("************************************************************")
print("******************* Tax with Dependents ********************")
print("************************************************************")

time.sleep(1)
while 1:
    try:
        AnnualIncome = float(input("Enter your annual income: "))
        
        dependents = int(input("Enter number dependents: "))
        
    except ValueError:
        print("incorrect values!")
        
    else:
        if AnnualIncome > 0:
            
            tax = AnnualIncome * 0.15
            
            if dependents >=3:
                reduction = "20%"
                tax = tax - tax * 0.2 
            elif dependents < 3 and dependents >=2:
                reduction = "10%"
                tax = tax - tax * 0.1
            else:
                reduction = "no"
                tax = tax
            print(f"you got {tax} taxes after {reduction} reduction")
        else:
            print("annual income must not be Zero ")
    finally:
        state = input("would you like yo use it again? (y / n)")
        if state == 'y':
            continue
        elif state == 'n':
            print("program complete")
            break
        else:
            break
