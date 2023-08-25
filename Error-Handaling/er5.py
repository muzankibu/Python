try:
    a=10
    b=10
    print(a+b)
except ValueError as e:
    print('There is value error')
else:
    print('No error!')