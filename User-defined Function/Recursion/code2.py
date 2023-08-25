def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
a=int(input("Enter your number:"))
print("Factorial:",factorial(a))