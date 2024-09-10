#there is no way to a value of tuple cant be changed or deleted
#adding new value to a yuple

a=('Apple', 'Orange', 1, 2, True, False)
a=a+(6,) #only a tuple can be aded to a tuple, if we dont use , than 6 will be considered as int value not tuple
print(a)
