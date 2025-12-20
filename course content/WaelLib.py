def add(a,b):
    sum = a+b
    return sum

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def power(a,b):
    return a**b

def div(a,b):
    if b != 0:
        div = a/b
        print ("Division = " ,div)
    else:
        print("we can't divide by zero")
