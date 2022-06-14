import operator
li=[]
x=int(input('How many num you want give?\nAnswer:'))
for i in range(0,x):
    a=int(input('Enter value num %d:'%(i+1)))
    li.append(a)
print('The values are respectively:',end='')
for i in range(0,x):
    print(li[i],end='')
operator.setitem(li,1,'New') 
print('\nAfter using setitem():',end='')
for i in range(0,x):
    print(li[i],end='')
operator.delitem(li,2)
print('\nAfter using delitem():',end='')
for i in range(0,x-1):
    print(li[i],end='')
print('\nAfter using getitem():',operator.getitem(li,1))    
