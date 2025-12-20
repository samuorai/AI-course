"""
Created on Wed Dec 18 18:14:29 2025

assignment #9 program #1
@author: comma

Create class Complex with Real and imaginary as private data members. Also, 
create two complex numbers from this class. Then Add, subtract and compute the 
magnitude of both. Please write the below class Complex and then use it as in the 
calling section.

"""
#%%
import math

class Complex:
    def __init__(self,R,I):
        self.__Real = R
        self.__Img = I
    #setters
    def setReal(self,R):
        self.__Real = R
    def setImg(self,I): 
        self.__Img = I
    
    def setComplex(self,R,I):
        self.__Real = R
        self.__Img = I
        
    #getters
    def getReal(self):
        return self.__Real
    def getImg(self):
        return self.__Img
    
    
        
    #add Complex
    def AddComplex(self, Other):
        return Complex(self.__Real + Other.getReal(),self.__Img + Other.getImg())
    
    #subtract
    def SubtractComplex(self,Other):
        return Complex(self.__Real - Other.getReal(),self.__Img - Other.getImg())
    
    #Magnitude
    def Magnitude(self):
        return math.sqrt(pow(self.__Real,2) + pow(self.__Img,2))
    
    def printComplex(self):
        print("Real Part = ",self.__Real)
        print("Imaginary Part = ",self.__Img)
        
#%%
#calling

c1 = Complex(20,50)
c2 = Complex(60,90)

print("---------- AddComplex ---------")
c3 = c1.AddComplex(c2)
c3.printComplex()

print("---------- SubtractComplex ---------")
c4 = c1.SubtractComplex(c2)
c4.printComplex()
print("---------- SubtractComplex ---------")
print("Magnitude of C1 = ",c1.Magnitude())


