l1=[]
l2=[]
l3=[]
s=0
a=int(input('How many number do you want to enter?\nAnswer:'))
for i in range(0,a):
	x=int(input('Enter the intiger num %d:'%(i+1)))
	l1.append(x)
for j in range(0,a):
	if l1[j]%5==0:
		l2.append(l1[j])
	else:
		l3.append(l1[j])
		s=s+1	
print('\nIs all given number dividable by 5?')
if s>0:
	print(f'No! {s} numbers can\'t be divide by 5 which are:{l3}. The dividable numbers are:{l2}')
else:
	print(f'Yes! All {a} numbers can be divide by 5 which are:',l1)