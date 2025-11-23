# -*- coding: utf-8 -*-
"""
assignement #2
date: 26 - 10 - 2025
authored by Wael Badr
program #1
compute the area of a circle from a user provided radius.
"""

import time 

print ("******** welcom to circle area calculator ********\n")
time.sleep(1)
R = float(input("Enter radius to calculate: "))
print("\n")
area = 3.1416 * R**2
print (f"The area of the circle is {area:0.2f} square units.\n")

print ("***************************************************")