inp = input("enter a string: ")
output = "hello " + inp
with open('output5.1.txt', 'w') as f:
    f.write(output)
    f.close()