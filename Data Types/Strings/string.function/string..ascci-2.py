import string
def check(value):
	for letter in value:
		if letter not in string.ascii_letters:
			return 0
	return 1
s=str(input('Enter your string:'))
x=check(s)
if x==1:
	print('c')
else:
	print('nc')
