print("Hello")
print("Enter the charecter:",end=" ")
c=input()
print(c)

if c >= 'a' and c<='z':
    print("It's an lower case charecter!")
elif c>= 'A' and c<='Z':
    print("It's a upper case charecter!")
else:
    print("It's not a charecter type input!")