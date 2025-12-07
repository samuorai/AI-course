# -*- coding: utf-8 -*-
"""
Created on Sun Nov  24  2025
assignment #6 program #2

@author: Wael Badr

Write these parts of the code and print the obtained results
"""

#%%
# 1.
list3 = [10,20,30,40,50]
print(list3)
print("---------------------------------------")
list3.insert(0,10000)
print(list3)
print("---------------------------------------")
list3.insert(3,20000)
print(list3)

print("***************************************")

# 2.
list3.remove(10000)
print(list3)
print("---------------------------------------")
list3.remove(20000)
print(list3)

#%%
# 3.

for i in range(1000,1010):
    list3.append(i)

print(list3)
print("---------------------------------------")
list3.pop()
print(list3)
print("---------------------------------------")
list10 = list3.copy()
print(list10)

#%%
# 4.

list5 = [10, 100,17,50,90]
print(list5)
print("---------------------------------------")
list5.sort()
print(list5)
print("---------------------------------------")
list5.sort(reverse = True)
print(list5)
print("---------------------------------------")
print(len(list5))
print("---------------------------------------")
print(sum(list5))
print("---------------------------------------")
print("average = ",sum(list5)/len(list5))

#%%
#5.

list7 = [10,50,70]

try:
    print(list.index(100))
except:
    print("Item is not found")