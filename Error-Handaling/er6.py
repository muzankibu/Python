try:
    a=10
    b=10
    print(a+b)
except ValueError as e:
    print('There is name error')
finally:
    print('I will execute whether there is error or not!')