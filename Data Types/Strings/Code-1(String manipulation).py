from colorama import Fore

print(Fore.GREEN +'Color: Green')
a='bangla'
b='DESH'
c='Bangladesh is my motherland'
d='cHiTTagonG'
e='Kolkata komola Kanter Khonista konna kakali!'
print(a+b)
print(type(a))
print('Bangladesh')
print("Bangladesh")
print('Bangladesh is my \'motherland\',I love her so much')
print('Bangladesh is my \"motherland\",I love her so much')
print('Bangladesh is my \\motherland\\,I love her so much')
print('Bangladesh is my \nmotherland\t,I love her so much')
print(a[0],a[1])
print(c[0:5])
print(c[-1])
print(a+'-'+b+'-'+c)
print('-'.join((a,b,c)))
print(a.capitalize())
print(a.upper())
print(a.lower())
print(b.casefold())
print(d.swapcase())
print(c.title())
print(len(c),'|Space also to be counted|')
x=e.count('k')
y=e.count('K')
print(x+y)
	
