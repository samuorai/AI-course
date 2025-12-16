"""
Created on Mon Dec  1 01:48:20 2025

assignment #7 program #2 task #6

@author: wael badr

Task 6: Open a file data.txt on your hard-disk for: 
"""
# reading Data.txt file (file created)
try:
    file = open(r"C:\Users\comma\Documents\assignment_7\assign7p2_task6\Data.txt","r")
    line = file.read()
    print(line)
    file.close()
except:
    print("file is not accessable..")

# Open the file for append:

try:
    file = open(r"C:\Users\comma\Documents\assignment_7\assign7p2_task6\Data.txt","a")
    file.write("\n HHHHHHHHHHHHHH")
    file.close()
except:
    print("file is not accessable..")
    
    
# Open the file for writing:

try:
    file = open(r"C:\Users\comma\Documents\assignment_7\assign7p2_task6\Data.txt","w")
    file.write("\n HHHHHHHHHHHHHH")
    file.close()
except:
    print("file is not accessable..")