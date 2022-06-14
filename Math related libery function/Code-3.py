def Sohan(x):    
    import operator
    li=[]
    for i in range(0,x):
        a=int(input('Enter value num %d:'%(i+1)))
        li.append(a)
    print('The values are respectively:',end='')
    for i in range(0,x):
        print(li[i],end='')
    operator.setitem(li,slice(3,6),['Happy','New','Year']) 
    print('\nAfter using setitem():',end='')
    for i in range(0,x):
        print(li[i],end='')
    operator.delitem(li,slice(1,3))
    print('\nAfter using delitem():',end='')
    for i in range(0,x-3):
        print(li[i],end='')
    print('\nAfter using getitem():',end='')
    operator.getitem(li,slice(1,4))
    for i in range(1,x-3):
        print(li[i],end=' ')

def test():
    a=int(input('You must give 7 or more than 7 inputs!\nSo now, How many num you want to store?\nAnswer:'))
    if a>=7:
        Sohan(a)
    else:
        test()
test()        