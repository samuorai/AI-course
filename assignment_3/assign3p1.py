# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:06:36 2025
assignment #3 program #1

@author: Wael Badr

performing all arithmatic operations (+ , - , * , / , // , % , ** ) and print with clear label , check for division by
zero before performing print error message if second number is zero
"""
import time

print("************************************************************")
print("**************** arithmatic operations *********************")
print("************************************************************")

time.sleep(1)
while 1:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        Sum = num1 + num2
        sub = num1 - num2
        multi = num1 * num2
        div = num1 / num2
        fdiv = num1 // num2
        rem = num1 % num2
        Pow = num1 ** num2
        
    
    except ZeroDivisionError:
        print("second number must NOT be a Zero.")
   
    except TypeError:
        print("use numbers only.")
        
    else:
        print("add = ",Sum)
        print("sub = ",sub)
        print("multiply = ",multi)
        print("division = ",div)
        print("floor division = ",fdiv)
        print("remainder = ",rem)
        print("power = ",Pow)
        
    finally:
        state = input("do you want to use it again? (y / n)")
        if state.lower() == 'y':
            continue
        elif state.lower() == 'n':
            print("program complete")
            break
        else:
            break
        