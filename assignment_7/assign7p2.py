# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 01:24:29 2025

assignment #7 program #2

@author: Wael Badr
"""

# Task 1:  Adding and subtracting two 1D arrays:
    
import numpy as np

arr1 = np.array([1,2,3,4,5,10])

print(arr1.dtype)

print(arr1.shape)

arr2 = np.array([1,2,3,4,5,10])

print(arr1.shape)
print(arr2.shape)

arr_s = arr1 + arr2
arr_sub = arr1 - arr2

print(arr_s)
print(arr_sub)
print("-------------------------------")

# Task 2: Converting Array from type to another type:

arr2 = np.array([1,2,3,4,5,10])
arr3 = arr2.astype(float)
print(arr3)
print(arr3.dtype)
print("-------------------------------")

# Task 3: Array reshaping from 1D to 2D:
    
arr4 = np.array([1,2,4,1,4,10])
print(arr4.shape)

arr5 = arr4.reshape(2,3)
print(arr5)
print(arr5.shape)
print("-------------------------------")

# Task 4: Operation on Arrays:
    
arr1 = np.array([1,2,3,4,5,10])

print(arr1.sum())
print(arr1.mean())
print(arr1.max())
print(arr1.min())

print(arr1[0])

print(arr1[-1])

for item in arr1:
    print(item)
    
for i in range(0,len(arr1)):
    print(arr1[i])
    