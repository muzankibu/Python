f='kakali kakare koi kaka kake keno khakha kore!'
l=[]
print(f.count('k',5,20))
q=len(f)
for i in range(0,q):
	s=str(f[i])
	if s=='k':
		l.append(i)
	else:
		continue
print(l)	
print(f.replace('k','j'))
print(f.replace(' ',''))
print(f.strip('!'))
print(f.split(' '))