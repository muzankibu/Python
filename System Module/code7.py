import sys 

s=sys.stdin
for line in s: 
	if 'q' == line.rstrip(): 
		break
	print(f'Input : {line}') 

print("Exit") 
