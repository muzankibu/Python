def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("Calculator for two number")
a=float(input("Enter your first number:"))
b=float(input("Enter your second number:"))
print("Addition:",add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))