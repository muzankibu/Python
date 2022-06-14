a=[0,1,2,3,4,5,6,7,8,9]
new_a=[a[i]**2 for i in range(len(a)) if a[i]%2==0]
print(new_a)