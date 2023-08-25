def add(**var):
    temp=0
    print(type(var))
    for i in var:
        temp=temp+var[i]
    print(temp)
add(a=1,b=2,c=3)