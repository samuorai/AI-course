# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:06:36 2025
assignment #3 program #9

@author: Wael Badr

Write a sequential program that takes the principal amount, annual
interest rate (as a decimal), and time (in years) as input. 
Calculate the simple interest using the formula (principal * rate *
time) / 100, and print the result. Ensure proper input validation with try-except.
"""

import time

print("************************************************************")
print("**************** Simple Interest Calculator ****************")
print("************************************************************")

time.sleep(1)
while 1:
    try:
        Pamount = float(input("Enter the principal amount: "))
        
        AinterestRate = float(input("Enter the annual interest rate: "))
        
        year = int(input("Enter the year: "))
        
    except ValueError:
       print("incorrect values!")
   
    else:  
       if year > 0 and Pamount > 0 and AinterestRate > 0:
           
           simple_interest =  (Pamount * AinterestRate * year) / 100
        
           print(" Simple interest = ",simple_interest)
       else:
           print("incorrect inputs")
            
    
    finally:
        
        state = input("would you like to try again? (y / n)")
        
        if state == 'y':
            continue
        elif state == 'n':
            print("program complete")
            break
        else:
            break