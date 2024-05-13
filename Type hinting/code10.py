from typing import NewType

Userld2 = int
print(Userld2(10))

def find_user(user_id: Userld2):
    print('Found:', user_id)
find_user(Userld2(10))
find_user(100)
print('..............................................')

Userld2 = NewType('Userld', int)
print(Userld2(10))

def find_user(user_id: Userld2):
    print('Found:', user_id)

find_user(Userld2(10))
find_user(100)
#use mypy for understanding

