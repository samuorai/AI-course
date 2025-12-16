import math
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
        
# ------------------------------------------------------
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
# ------------------------------------------------------
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