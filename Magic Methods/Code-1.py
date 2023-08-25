a=6
b=5

print(a.__eq__(b))
print(a.__ne__(b))
print(a.__lt__(b))
print(a.__le__(b))
print(a.__gt__(b))
print(a.__ge__(b))

print('...............................')
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
#print(a.__div__(b))
print(a.__mod__(b))
print(a.__pow__(b))
print(a.__floordiv__(b))

print('................................')

a=5
print(type(a))
a=a.__float__()
print(type(a))
a=a.__str__()
print(type(a))
a=a.__repr__()
print(type(a))

print('................................')


a='Bangladesh'
b='desh'
print(a.__len__())
print(a.__iter__())
print(list(a.__iter__()))
print(a.__contains__(b))



