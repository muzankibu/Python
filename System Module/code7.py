import sys 

limit = int(input('What should be the depth of Python interpreter stack '))

sys.setrecursionlimit(limit)

print('The depth of stack is', sys.getrecursionlimit())

