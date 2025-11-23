# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 20:06:36 2025
assignment #3 program #7

@author: Wael Badr

Write a program that takes a score
(0100) as input and uses an if-elif-else structure to assign a grade: A (90+),
B (8089), C (7079), or Fail (below 70). Print the grade with a message (e.g.,
"Grade: A"). Use try-except for invalid inputs and ensure proper indentation.
"""

import time

print("************************************************************")
print("***************  if-elif-else Grading System ***************")
print("************************************************************")

time.sleep(1)
while 1:
    try:
        mark = float(input("Enter your mark: "))
    except ValueError:
        print("invalid input!")
    else:
        if mark <= 100 and mark >= 90:
            Grade = "A"
        elif mark < 90 and mark >= 80:
            Grade = "B"
        elif mark < 80 and mark >= 70:
            Grade = "C"
        else:
            Grade = "D"
        print("Your grade is: ", Grade)
    finally:
        state = input("would you like to try again? (y / n)")
        if state.lower() == 'y':
            continue
        elif state.lower() == 'n':
            print("program complete")
            break
        else:
            break