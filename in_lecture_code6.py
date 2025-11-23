#%%
#type 1
def add_1(a,b):
    sum = a+b
    return sum
    
#calling 
sum = add_1(5,5)
print("sum = ", sum)

#%%
#typ2

def add_2(a,b):
    sum = a+b
    print("sum = ", sum)
    
#calling

add_2(2,4)

#%%
#type 3

def add_3():
    a= float (input("Enter first number: "))
    b= float (input("Enter second number: "))
    sum = a+b
    return sum

#calling

sum = add_3()
print ("sum = ",sum)

average = sum /2

print("average = ", average)

#%%

#type 4
def add_4():
    a= float (input("Enter first number: "))
    b= float (input("Enter second number: "))
    sum = a+b
    print("sum = ",sum)
#calling
add_4()

#%%

def ComputeGrade(d1,d2,d3):
    if (d1 >= 0 and d1 <=10) and (d2 >= 0 and d2 <=10) and (d3 >= 0 and d3 <=10):
        total = d1 + d2 + d3
        percentage = total / 30 * 100
        if percentage >= 85 and percentage <=100:
            print("Grade: Excellent")
        elif percentage >= 75 and percentage < 85:
            print("Grade: very good")
        elif percentage >= 65 and percentage < 75:
            print("Grade: good")
        elif percentage >= 50 and percentage < 65:
            print("Grade: pass")
        else: 
            print("Fail")
    else:
        print("You must enter your three degrees betweetn 0 and 10")
#calling
for i in range(1, 5):
    print("Enter three degrees of student ", i)
    d1 = float(input("Enter first degree: "))
    d2 = float(input("Enter second degree: "))
    d3 = float(input("Enter third degree: "))
    ComputeGrade(d1,d2,d3)
    
#%%
list1 = [10,20,30,40,50]

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

print(list1)

for item in list1:
    print(item)
    
for i in range(0, len(list1)):
    print(list1[i])
#%%

list2 = [100,10,70,90]

print(list2)

list2[0] = 200

list2[3] = 1000

list2.append(10000)

print(list2)

list2.append("wael")

list2.append(3.5)
list2.append(True)

print(list2)

for item in list2:
    print(item)

#%%

list3 = [10,20,30,40,50]

print(list3)

list3.insert(0,1000)
list3.insert(3,20000)

print(list3)

list3.remove(20000)
print(list3)

for i in range(1000,1010):
    list3.append(i)

print(list3)

list3.pop()
print(list3)

list10 = list3.copy()

print(list10)

list10.clear()
print(list10)

list5 = [10, 100,17,50,90]

list5.sort()
print(list5)

list5.sort(reverse = True)
print(list5)

print(len(list5))
print(sum(list5))
print("average = ",sum(list5)/len(list5))

list7 = [10,50,70]

try:
    print(list.index(100))
except:
    print("Item is not found")