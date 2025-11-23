# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9  2025
assignment #4 program #3

@author: Wael Badr

Write a program to print numbers 1-20, skipping those divisible by 5 using continue.

"""

import time

print("************************************************************")
print("*************** skipping divide by 5 to continue ***********")
print("************************************************************")

time.sleep(1)
i = 1
while (i <= 20):
      if i%5 == 0:
          i = i + 1
          continue
      print(i)
      i = i + 1
time.sleep(3)