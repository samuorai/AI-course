
"""
Created on Sun Nov 30 11:00:03 2025

assignment #7 program #1

@author: Wael Badr
"""
# 1. create the following:
import numpy as np
l1 = [10,20,30,40,50]
t1 = ("Ali","Sara","Omar")
dic1= {"Name":"Hany","Age":42,"Department":"computer science"}
s1= {2,4,6,8}
arr1= np.array([1,3,5,7,9])

# 2. print all data structure clearly, each with a proper label:
print(l1)
print(t1)
for key,value in dic1.items():
    print(key," : ",value)
print(s1)
print(arr1)

# 3. perform one operation on each:
    #add new number to the list.
l1.append(70)
print(l1)

#----------------------------------

# Count how many times a name appears in the tuple. 

print(t1.count("Ali"))

#----------------------------------
# add a new key-value pair "job":"professor" in the dictionary.

dic1.update({"job":"professor"})
print(dic1)

#----------------------------------
# Check whether the number 4 exists in the set. 
print(4 in s1)
#----------------------------------
#  Compute and print the sum of all elements in the NumPy array. 

print(sum(arr1))