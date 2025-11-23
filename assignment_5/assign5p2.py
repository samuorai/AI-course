# -*- coding: utf-8 -*-
"""
Created on Sun Nov  18  2025
assignment #5 program #2

@author: Wael Badr

Create a python function that receives student three degrees and print his/her grade.
"""
def ComputeGrade():
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