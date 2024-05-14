#some functions of dictionary

#copy--
a={'name': 'Soleman Hossain', 'nickname':'Shourobh', 'email': 'shourobh@gmail.com', 'phone':'01234567899'}
print(a.copy())

#get(key, default=None)
a={'name': 'Soleman Hossain', 'nickname':'Shourobh', 'email': 'shourobh@gmail.com', 'phone':'01234567899'}
print(a.get('name'))
print(a.get('hometown','Not Mentioned'))

#key in dictionary
print('name' in a)

#items(), keys() and values() in dictionary
print(a.items())
print(a.keys())
print(a.values())
