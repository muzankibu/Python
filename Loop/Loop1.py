lm=int(input())
n=1
s=0
while n<=lm:
    if n==lm:
        print(f'{n}',end='=')
    else:
        print(f'{n}',end='+')
    s=s+n
    n=n+2

print(s)