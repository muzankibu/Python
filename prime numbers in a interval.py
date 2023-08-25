a=int(input('Enter lower bound:'))
b=int(input('Enter upper bound:'))


for i in range(a,b+1):
	if i>=2:
		for j in range(2,i):
			if (i%j==0):
				break
		else:
			print(i)
	else:
		print('0 and 1 cannot inputed!')			