# -*- coding: utf-8 -*-
"""
rectangle area
Created on Sat Oct 18 22:34:13 2025

@author: Wael osama"""

celsius = float(input("Enter the degree: "))
kelvin = celsius + 273
print ("kelvin degree is : ",kelvin)


""" refined code
print("welcome to temperature converter")

choice = input ("choose conversion type: \n 1. Celsius to Kelvin \n 2. Kelvin to Celsius \n Enter choice: ")
if choice == '1':
# Celsius to Kelvin conversion
    celsius = float(input("Enter the temperature in Celsius: "))
    kelvin = celsius + 273.15
    print("The temperature in Kelvin is:", kelvin)
# Kelvin to Celsius conversion
elif choice == '2' :
    kelvin = float(input("Enter the temperature in Kelvin: "))
    celsius = kelvin - 273.15
    print("The temperature in celsius is:", celsius)
else:
    print("Invalid choice. Please select 1 or 2.")
    """
