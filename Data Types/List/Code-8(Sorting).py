a=[8,2,6,10,4,3,5,8,1,0,6,4,9,8]
a.sort()
print(a)
b=['Showrav','!','1','0','9']
b.sort()
print(b)
print('................................................')

numbers = [1, 3, 4, 2]
numbers.sort(reverse=True)
print(numbers)
decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68]
decimalnumber.sort(reverse=True)
print(decimalnumber)
words = ["Geeks", "For", "Geeks"]
words.sort(reverse=True)
print(words)
print('...................................................')

l=['aaa','a','aa','aaaaa','aaaaaa','aaaa']
l.sort(key=len)
print(l)
print('...................................................')
l2=[(3,2),(1,4),(7,6)]
def sortbysec(x):
	return x[1]
l2.sort(key=sortbysec)
print(l2)	
