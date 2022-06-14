print('Index-1\n...........')
l=[1,2,3,4,5,3,4]
print(l.index(4))
l2= ['cat','dog','tiger','cat','moose']
print(l2.index('cat'))
print('\n')
print('Index-2\n............')
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
print(list1.index(4, 4, 8))
print(list1.index(1, 1, 7))
list2 = ['cat', 'bat', 'mat', 'cat', 'get', 'cat', 'sat', 'pet']
print(list2.index('cat', 2, 6 ))
print('\n')
print('Index-3\n........')
list1 = [1, 2, 3, [9, 8, 7], ('cat', 'bat')]
print(list1.index([9, 8, 7])) 
print(list1.index(('cat', 'bat')))
print('\n')
print('Index-4\n........')