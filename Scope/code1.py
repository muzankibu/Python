x=10
def print_():
    global x  #try without the 'global' keyword to see the difference how both 'x' are not the same 
    x= 20
    print(x,  id(x))

print_()
print(x,  id(x))

