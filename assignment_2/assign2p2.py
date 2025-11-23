# -*- coding: utf-8 -*-
"""
assignement #2
date: 26 - 10 - 2025
authored by Wael Badr
program #2
compute the area of a cconvert a temperature from Fahreheit to celsius.
"""

import time

print ("######## Temperature converter ########")
time.sleep(1)

temp = float(input("Enter temp. in Fahrenhiet: "))

cel = (temp - 32)*5/9
print(f"{temp:0.2f} F is {cel:0.2f} C")

print("########################################")
