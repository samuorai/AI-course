# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 18:14:29 2025

assignment #8 program #2
@author: comma
create a program that :
    1. opens file.txt in write mode and writes any content.
    2. opens the same file in append mode and adds more content.
    3. opens the same file in read mode and prints its full contents to the screen.

"""



try:
    file =  open(r"C:\Users\comma\file.txt","w")

    file.write("hi, i'm wael osama")
    
    file.close()
except:
    print("Can't access this file")

#%%

try:
    file = open(r"C:\Users\comma\file.txt","a")
    file.write("\n i am 42 years old")
    file.close()
except:
    print("file is inaccessable")
    
#%%

try:
    file = open(r"C:\Users\comma\file.txt","r")
    line = file.read()
    print(line)
except:
    print("file is inaccessable")