"""
assignement #2
date: 26 - 10 - 2025
authored by Wael Badr
program #3
calculate the total fuel cost for a road trip.
"""

import time

print("@@@@@@@@ Trip fuel cost estimator @@@@@@@@\n")

time.sleep(1)
km = float(input("Enter distance in Kilometers: "))
print("\n")
fe = float(input("Enter fuel effeciency in Kilometers per liter: "))
print("\n")
price = float(input("Enter price per liter in EGP: "))
print("\n")
TotalCost = (km / fe) * price
print(f"Your trip will cost {TotalCost:0.2f} EGP\n")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
