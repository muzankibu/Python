l1=[]
l2=[]
l3=[]
s=0
a=int(input('How many number you want to test:'))
for i in range(0,a):
	x=int(input('Enter the intiger num %d:'%(i+1)))
	l1.append(x)
for i in range(0,a):
	if l1[i]%2==0:
		l2.append(l1[i]%2==0)
		l3.append(l1[i])
		s=s+1
	else:
		continue	
print('\nIs there anyy even number given?')
p=str(any(l2))
if p=='True':
	print(f'Yes! {s} even number. These are:',end='')
	print(l3)
else:
	print('No! There ain\'t a single even number.')

