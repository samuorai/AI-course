# -*- coding: utf-8 -*-
"""
Created on Sun Nov  18  2025
assignment #5 program #3

@author: Wael Badr

Create a python function that computes the cylinder volume.
"""
# 1. with internal function:

from math import pi, pow

def CylinderVolume(height , radius):
    volume = pi * pow(radius,2) * height
    return volume

height =float(input("Enter the height: "))
radius =float(input("Enter the radius: "))
if radius > 0 and height > 0:
    print(f"the volume of the cylinder = {CylinderVolume(height,radius):0.2f}")
else:
    print("Enter positive value for both height and radius")
#%%

# 2. with user defined function:
    
def CylinderVolume(height , radius):
    volume = 3.14159265359 * (radius**2) * height
    return volume

height =float(input("Enter the height: "))
radius =float(input("Enter the radius: "))


CylinderVolume(height , radius)

print(f"the volume of the cylinder = {CylinderVolume(height,radius):0.2f}")
