
#%%


num = int(input("Enter positive int number: "))
fact = 1

if (num == 0) or (num == 1):
    print(num, "!=", fact)
elif num > 0:
    for i in range(num, 0, -1):
        fact = fact * i
    print(num, "!=", fact)
else:
    print("you must enter positive number")

#%%
for count in range(0,5):
    num = int(input("Enter positive int number: "))
    fact = 1
    
    if (num == 0) or (num == 1):
        print(num, "!=", fact)
    elif num > 0:
        i = num
        while(i > 0):
            fact = fact * i
            i = i -1
        print(num, "!=", fact)
    else:
        print("you must enter positive number")
    
#%%
try:
    for count in range(0,5):
        num = int(input("Enter positive int number: "))
        fact = 1
        
        if (num == 0) or (num == 1):
            print(num, "!=", fact)
        elif num > 0:
            i = num
            while(i > 0):
                fact = fact * i
                i = i -1
            print(num, "!=", fact)
        else:
            print("you must enter positive number")
except:
    print("enter positive number not letters ..")
finally:
    print(" ----- END of the program ------")
    
#%%

import math as mt
print(mt.pow(2,2))
print(mt.sqrt(100))

#%%

from math import sqrt, pow

print(pow(2,2))
print(sqrt(100))
#%%
import numpy as np

arr1 = np.array([1,2,3,4])

print(arr1)

#%%

import math

print(math.power(2,3))

print(math.Pow(2,3))

print(math.pow(2,3,4,5,6))

print(math.pow(2,3))

#%%

def printNumber():
    for i in range(0,10):
        print(i)
printNumber()

#%%

def ComputeGrade():
    for i in range(1,4):
        print("Computing grades for student:")
        d1 = float(input("Enter first degree (0 - 10): "))
        d2 = float(input("Enter second  degree (0 - 10): "))
        d3 = float(input("Enter third degree (0 - 10): "))
        sum = d1+d2+d3
        print("total degree = ",sum)
        percent = sum / 30 * 100
        print ("percentage % = ",percent)
        if (percent >= 0 and percent <=100):
            if (percent >= 85 and percent <=100):
                print ("Excellent")
            elif (percent >= 75 and percent < 85):
                    print ("very good")
            elif (percent >= 65 and percent < 75):
                    print ("good")
            elif (percent >= 50 and percent < 65):
                    print ("pass")
            else:
                print ("failed")
        else:
            print (" you must put your grades")
    
ComputeGrade()
#%%

def ProductTable():
    for i in range(1,13):
        for j in range(1,13):
            print(i, " * ", j, " = ", i*j)
        print("------------------------------------")
ProductTable()
#%%
#type 1 takes parameters and return value.
def Rec_Area_1(width,length):
    area = width * length
    return area
w = float(input("Ener width: "))
l = float(input("Ener length: "))

area =  Rec_Area_1(w,l)
print ("Rectangle Area = ",area)
#%%
#type 2 takes parameters and return no value.
def Rec_Area_1(width,length):
    area = width * length
    print ("Rectangle Area = ",area)


w = float(input("Ener width: "))
l = float(input("Ener length: "))
Rec_Area_1(w,l)

print("---------- End ---------")

#%%
#type 3 doesn't take parameters and return value.
def Rec_Area_3():
    width = float(input("Ener width: "))
    length = float(input("Ener length: "))
    area = width * length
    return area
    
area = Rec_Area_3()

print ("Rectangle Area = ",area)

print("---------- End ---------")
#%%
#type 4 doesn't take parameters and return no value.
def Rec_Area_4():
    width = float(input("Ener width: "))
    length = float(input("Ener length: "))
    area = width * length
    print ("Rectangle Area = ",area)
    
area = Rec_Area_4()
print("---------- End ---------")

#%%
def sumNumbers(num1,num2,num3):
    return num1+num2+num3

num1 = float(input("Enter first number: "))
num2 = float(input("Enter first number: "))
num3 = float(input("Enter first number: "))

sum = sumNumbers(num1,num2,num3)
print("sum = ",sum)
