# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 15:24:33 2025

assignment #8 program #1

@author: wael badr

• Prompt the user to enter 4 course scores, each out of 10.
• Append each score to a list.
• Pass the list to a function that:
    o Computes the total (out of 40) and percentage.
    o Returns a textual grade: Excellent, Very Good, Good, Pass, or Fail.
• Print the list, total, percentage, and grade.
"""
import time
print("------------ Grade calculation program -------------")
time.sleep(1)
try:
    math = float(input("Enter your math score out of 10: "))
    physics = float(input("Enter your physics score out of 10: "))
    biology = float(input("Enter your biology score out of 10: "))
    english = float(input("Enter your english score out of 10: "))
    if math <= 10 and physics <= 10 and biology <= 10 and english <= 10:
        l1 = [math,physics,biology,english]
        grade = (sum(l1)*100)/40
        if grade <= 100 and grade > 85:
            print("Grade is : Excellent")
        elif grade <= 85 and grade > 75:
            print("Grade is : Very Good")
        elif grade <= 75 and grade > 65:
            print("Grade is : Good")
        elif grade <= 65 and grade >= 50:
            print("Grade is : pass")    
        else:
            print("Grade is : fail") 
            
        print("Thank you")
    else:
        print("Score limit is 10 points, please enter score from 0 o 10")
        
except ValueError:
    print("Wrong inputs! , please enter score from 0 to 10")