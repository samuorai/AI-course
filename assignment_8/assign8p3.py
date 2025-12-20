"""
Created on Wed Dec 17 18:14:29 2025

assignment #8 program #3
@author: comma

Write this Rectangle Class then create two objects from this class

"""

class Rectangle:
    # Constructor
    def __init__(self,w,l):
        if w > 0 and l > 0:
            self.__width = w
            self.__length = l
        else:
            print("you must enter positive numbers")
            self.__width = 0
            self.__length = 0
    
    # Getters or Accessors
    def getWidth(self):
        return self.__width
    
    def getLength(self):
        return self.__length
    
    #Setter or Modifires
    def setWidth(self,w):
        if w > 0:
            self.__width = w
        else:
            print("you must enter positive number")
            self.__width = 0
    def setLength(self,l):
        if l > 0:
            self.__length = l
        else:
            print("you must enter positive number")
            self.__length = 0
    
    def setWidthLength(self,w,l):
        if w > 0 and l > 0:
            self.__width = w
            self.__lenght = l
        else:
            print("you must enter positive numbers")
            self.__width = 0
            self.__lenght = 0
    
    def Area(self):
        return self.__width * self.__length
    
    def Perimeter(self):
        return 2 * (self.__width + self.__length)
    
    def Display(self):
        print("--- Rectangle Details ---")
        print("Width = ",self.__width)
        print("length = ",self.__length)
        print("Area = ",self.Area())
        print("Perimeter = ",self.Perimeter())
        print("===================================")
        
# calling
rect1 = Rectangle(3,2)

rect1.Display()

w= float(input("Enter width: "))
l= float(input("Enter length: "))

rect2 = Rectangle(w,l)
rect2.Display()