import operator
a='Devil'
b='evil'
print('Strings after concatenate:',operator.concat(a,b))
print(f'Does {a} contains {b}?\nAnswer:',end='')
if operator.contains(a,b):
	print('Yes')
else:
	print('No')	
