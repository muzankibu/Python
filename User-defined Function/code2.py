def add(*ins):
    print(type(ins))
    temp=0
    for i in ins:
        temp=temp+i
    print(temp)
add(1,2,3,4,5)