x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print(x if x>y else y)

x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))

x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)


x=int(input('Enter your number:'))
a=f'Yes! {x} an Even number'
b=f'No! {x} not a even number'
print(a if x%2==0 else b)

a, b = 1, 2
 
print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")

a, b = 10, 20 
# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't
# work if a is 0.
min = a < b and a or b
print(min)