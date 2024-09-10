f='kakali kakare koi kaka kake keno khakha kore!'
g="hello,fff,llolo,ggogo,ffff,bbb" 
l=[]
print(f.count('k'))
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
print(g.split(','))