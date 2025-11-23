# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9  2025
assignment #4 program #1

@author: Wael Badr

Write a program that checks if a person is eligible for a job: 
    age >=18 and experience >2 years
(nested inside age check). Print appropriate messages.
"""

import time

print("************************************************************")
print("****************** job eligibilty calculator ***************")
print("************************************************************")

time.sleep(1)
while 1:
    try:
        age = int(input("Enter your age: "))
        ex = int(input("Enter experince years: "))
    except ValueError:
        print("wrong input, please put your age.")
    else:
        if age >= 18:#nested condition
            if ex >= 2:
                print("you're'eligible for the job.")
            else:
                print("you ain't enough experince!")
        else:
            print("you ain't qualified!")
    finally:
        state = input("do you want to try again? (y / n): ")
        if state == 'y':
            continue
        else:
            print("thank you")
            break
        