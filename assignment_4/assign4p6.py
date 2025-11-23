
"""
Created on Sun Nov  9  2025
assignment #4 program #6

@author: Wael Badr

Write then run this Program to compute the grade of students

"""

import time

print("************************************************************")
print("************ Computing grades for students *****************")
print("************************************************************")

time.sleep(1)
hidden_num = 4
while 1:
    for i in range (1,4):
        print("Computing grades for student:",i)
        d1 = float(input("Enter first degree (0 - 10): "))
        d2 = float(input("Enter second  degree (0 - 10): "))
        d3 = float(input("Enter third degree (0 - 10): "))
        sum = d1 + d2 + d3
        print("total degree = ",sum)
        percent = sum / 30 * 100
        print (f"percentage = {percent:.2f} %")
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
    state = input("Do you want to compute another student grades? (y / n): ")
    if state == 'y':
        continue
    else:
        print("exiting ...")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        break