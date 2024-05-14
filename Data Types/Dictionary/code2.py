#Accessing, updating and removing dictinary

b=dict({'name': 'Sahil Hossain', 'nickname':'Saad', 'email': 'saad@gmail.com', 'phone':'01234556789'})
print(b)
b['name']='Muhammad Sahil Hossain'
print(b)
b['hometown']='Chittagong'
print(b)
c={'company':'Google', 'id':'2021682'}
c.update(b)
print(c)
del c['hometown']
print(c)
c.clear()
print(c)
