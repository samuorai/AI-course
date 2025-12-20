# -*- coding: utf-8 -*-

   
"""
    
for i in range (1,4):
    
    print("Computing grades for student:",i)
    
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
        
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
oddsum = 0
Evensum = 0
for i in range(0,21):
    if i % 2 == 0:
        Evensum = Evensum + i
    else:
        oddsum = oddsum + i
print("Evensum = ", Evensum)
print("oddsum = ",oddsum)

for i in range(0,11):
    if i == 3 :
        break 
    print (i)
print("out of loop")


for i in range(0,13):
    print("production table of ",i)
    for j in range(0,13):
        print (i," * ", j, " = ",i*j)
    print("-----------------------------------")
    
start = int(input("Enter start: "))
End = int(input("Enter end: "))
step = int(input("Enter step: "))

for i in range(start,End,step):
    print(i)
x = 10
while (x > 3):
    print (x)
    x = x - 1
print("out of while ...")"""





