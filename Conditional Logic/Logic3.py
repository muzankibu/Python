a=int(input())
b=a 
tmp=a//1000
print(tmp,'1000 tk notes')
if tmp>0:
    a=a%1000
    b=a
else:
    a=b
tmp=a//500
print(tmp,'500 tk notes')
if tmp>0:
        a=a%500
        b=a
else:
    a=b
tmp=a//100
print(tmp,'100 tk notes')
if tmp>0:
    a=a%100
    b=a
else:
        a=b
tmp=a//50
print(tmp,'50 tk notes')
if tmp>0:
    a=a%50
    b=a
else:
    a=b
tmp=a//20
print(tmp,'20 tk notes')
if tmp>0:
    a=a%20
    b=a
else:
    a=b
tmp=a//10
print(tmp,'10 tk notes')
if tmp>0:
    a=a%10
    b=a
else:
    a=b
    tmp=a//5
    print(tmp,'5 tk notes')
    if tmp>0:
        a=a%5
        b=a
    else:
        a=b
    tmp=a//2
    print(tmp,'2 tk notes')
    if tmp>0:
        a=a%2
        b=a
    else:
        a=b
    tmp=a//1
    print(tmp,'1 tk notes')
            
