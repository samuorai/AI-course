# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 19:27:52 2025

@author: comma
"""
import pandas as pd
import numpy as np

arr1 = np.array([[1,2,10],[10,4,5],[4,6,7]])
print (arr1)
print (arr1.shape)

arr2 = np.array([[1,2,10],[10,4,5],[4,6,7],[2,4,5]])
print (arr2)
print (arr2.shape)
arr3 = np.array([[1,2,10],[10,4,5],[4,6,7],[4,6,7],[4,6,7]])
print (arr3)
print (arr3.shape)

#vertical stacking
Combined_dataset = np.vstack((arr1,arr2,arr3))
print(Combined_dataset)
print(Combined_dataset.shape)

#%%

arr1 = np.array([[1,2,10],[10,4,5],[4,6,7]])
print (arr1)
print (arr1.shape)

arr2 = np.array([[1,2,10,11,11],[10,4,5,10,10],[4,6,7,11,11]])
print (arr2)
print (arr2.shape)

Combined_dataset1 = np.hstack((arr1,arr2))
print(Combined_dataset1)
print(Combined_dataset1.shape)

#%%

# linear aljebra

arr1 = np.array([[1,2,3],[4,5,6]])
print("\n Array 1:\n",arr1)
print(arr1.shape)

arr2= np.array([[10,20,30],[40,50,60]])
print("\n Array 2:\n",arr2)
print(arr2.shape)

print("Adition")
print(np.add(arr1,arr2))

print("Subtraction")
print(np.subtract(arr1,arr2))

print("Element wise Multiplicaton")
print(np.multiply(arr1,arr2))

print("Element Wise Division")
print(np.divide(arr1,arr2))

print("Dot product (Matrix Multiplication)")
print(np.dot(arr1,arr2.T))

#%%

# Statistical operations

#%%
# reading and writing with 
with open(r"D:\python_course\AI-course\data.txt","w") as file2:
    file2.write("Name: Hany Aly\n")
    file2.write("Age: 42 \n")
    file2.write("job: Assoc. prof.\n")
    
    lines = ["Hello world\n","Welocme\n","I am here\n"]
    file2.writelines(lines)
    
# read
with open(r"D:\python_course\AI-course\data.txt","r") as file3:
    content= file3.read()
    
    print(content)

with open(r"D:\python_course\AI-course\data.txt","a") as file2:
    content= file2.write("----------------------------")
    lines=["any aly\n","malak hany\n","aly mohamed\n"]
    file2.writelines(lines)
#%%

df_csv = pd.read_csv(r"D:\python_course\AI-course\data.csv")

print(df_csv.head())

print(df_csv.info())

print(df_csv.describe())

#%%

df_xlsx = pd.read_excel(r"D:\python_course\AI-course\dataX.xlsx",sheet_name="Sheet1")

print(df_xlsx.head())

print(df_xlsx.info())

print(df_xlsx.describe())
#%%

# OOP

