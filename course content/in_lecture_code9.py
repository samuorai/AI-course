# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 19:27:35 2025

@author: comma
"""
#%%
class Student:
    #constructor
    def __init__(self,name,age,job):
        self.__Name = name
        self.__Job = job
        
        if age > 0:
            self.__Age = age
        else:
            self.__Age = 0
            print("You must enter positive numeric value for age! ")
    #Getters or Acccessors
    def getName(self):
        return self.__Name
    def getJob(self):
        return self.__Job
    def getAge(self):
        return self.__Age
    
    #Setters or Modifires
    def setName(self, name):
        self.__Name = name
    def setAge(self, age):
        if self.__Age > 0:
            self.__Age = age
        else:
            self.__Age = 0
            print("You must enter positive numeric value for age! ")
        
    def setJob(self, job):
        self.__Job = job
    
    
    def setStudent(self , name, age, job):
        self.__Name = name
        self.__Job = job
        
        if age > 0:
            self.__Age = age
        else:
            self.__Age = 0
            print("You must enter positive numeric value for age! ")
    
    def PrintStudent(self):
        print("student name: ", self.__Name)
        print("student Age: ", self.__Age)
        print("student Job: ", self.__Job)
   
        
#calling 
s1 = Student("Hany Aly",41,"Assoc. prof")

print("Student Age is ", s1.getAge())

s1.setAge(43)

print("Student Age is ", s1.getAge())

s1.PrintStudent()


name = input("Enter your name: ")
age = float(input("Enter your age:"))
job = input("Enter your job: ")

s2 = Student(name, age, job)

s2.PrintStudent()
#%%

class Cylinder:
    #Constructor
    
    def __init__(self, rad, hig):
        if rad > 0 and hig > 0:
            self.__Radius = rad
            self.__Height = hig
        else:
            self.__radius = 0
            self.__height = 0
            print("Enter positive values for both radius and height")
    
    #getters
    def getRadius(self):
        return self.__Radius
    def getHeight(self):
        return self.__Height
    #def setters 
    
    def setRadius(self, rad):
        if rad > 0:
            self.__Radius = rad
        else:
            self.__Radius = 0
            print("Enter positive value for radius!")
    def setHeight(self, hig):
        if hig > 0:
            self.__Height = hig
        else:
            self.__Height = 0
            print("Enter positive value for height!")
    
    def setCylinder(self, rad, hig):
        if rad > 0 and hig > 0:
            self.__Radius = rad
            self.__Height = hig
        else:
            self.__radius = 0
            self.__height = 0
            print("Enter positive values for both radius and height")
    def Area(self):
        return 2* 3.14 * self.__Radius * self.__Height
    def Volume(self):
        return 3.14 * self.__Radius * self.__Height
    
    
    def PrintCylinder(self):
        print("Cylinder Radius = ", self.__Radius)
        print("Cylinder Radius = ", self.__Height)
        print("Cylinder Radius = ", self.Area())
        print("Cylinder Radius = ", self.Volume())
        
#calling

cyl1 = Cylinder(4,10)

cyl1.PrintCylinder()

print("------------------------------------------------")

rad = float(input("Enter positive value for radius: "))
hig = float(input("Enter positive value for height: "))

cyl2 = Cylinder(rad, hig)

cyl2.PrintCylinder()
        
#%%

class BankAccount:
    def  __init__(self, ctN, AccN, Mob,Nat, NID, bal):
        self.__CustomerName = ctN
        self.__AccountNumber = AccN
        self.__Mobile = Mob
        self.__Nationality = Nat
        self.__NationalID = NID
        self.__Balance = bal
    
    def getCustomerName(self):
        return self.__CustomerName
    def getACCuount(self):
        return self.__AccountNumber
    def getMobile(self):
        return self.__Mobile
    def getNationality(self):
        return self.__Nationality
    def getNationalID(self):
        return self.__NationalID
    def getBalance(self):
        return self.__Balance
    
    def setCustomerName(self,ctN):
        self.__CustomerName = ctN
    def setACCuount(self,AccN):
        self.__AccountNumber = AccN
    def setMobile(self,Mob):
        self.__Mobile = Mob
    def setNationality(self,Nat):
        self.__Nationality = Nat
    def setNationalID(self,NID):
        self.__NationalID = NID
    def setBalance(self,bal):
        self.__Balance = bal
    
    def setProfile(self)

#%%
import math
class Complex:
    #Constructor
    def __init__(self, r, img):
        self.__Real = r
        self.__Img = img
    
    #Getters
    def getReal(self):
        return self.__Real
    def getImg(self):
        return self.__Img
    
    #setters
    def setReal(self, r):
        self.__Real = r
    def setImg(self, img):
        self.__Img = img
    
    def setComplex(self, r, img):
        self.__Real = r
        self.__Img = img
        
        #Add Complex
    def Add(self, C2):
        real = self.__Real + C2.__Real
        img = self.__Img + C2.__Img
        if img > 0:
            print(real, "+J",img)
        else:
            print(real, "-J",-1*img)
    def Subtract(self, C2):
        real = self.__Real - C2.__Real
        img = self.__Img - C2.__Img
        if img > 0:
            print(real, "-J",img)
        else:
            print(real, "-J",-1*img)
        
    #Magnitude
    def MagintudeComplex(self):
        mag = math.sqrt(self.__Real **2 + self.__Img**2)
        return mag
    #print
    def PrintComplex(self):
        if self.__Img > 0:
            print(self.__Real, "+J", self.__Img)
        else:
            print(self.__Real, "-J",-1*self.__Img)
    
C1 =Complex(10,10)
C2 = Complex(20,20)

C1.PrintComplex()
C2.PrintComplex()
print("----------------------------------")
print("------- Add Complex ------")
C1.Add(C2)
print("----------------------------------")
print("------- subtract Complex ------")
C1.Subtract(C2)

print("Magnitude C1 ",C1.MagintudeComplex())




