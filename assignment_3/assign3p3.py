# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:06:36 2025
assignment #3 program #3

@author: Wael Badr

Write a program to test the following
statements about arithmetic operators and data types using try-except blocks.
For each, attempt the operation, catch any errors, and print whether the
statement is True or False with a brief explanation.
"""

import time

print("************************************************************")
print("**************** Data Type Compatibility *******************")
print("************************************************************")

time.sleep(1)

try:
   result = "5" + "3"
   print("Addition works on strings: true, Result = ",result)
except:
   print("Addition works on strings: false, operation not valid")
try:
   result = "hello" * 3
   print("Multiplication works on strings: true, Result = ",result)
except:
   print("Multiplication works on strings: false, operation not valid")
try:
   result = "10" / "2"
   print("Division works on strings: true, Result = ",result)
except:
   print("Division works on strings: false, operation not valid on strings")
try:
    result = 5 + 3.2
    print("Addition works on strings: true, Result = ",result)
except:
    print("Addition works on strings: false, operation not valid on floats")
try:
    result = 2.5 ** 2
    print("Exponentiation works on strings: true, Result = ",result)
except:
    print("Exponentiation works on strings: false, operation not valid on floats")
        
        
print("program complete")