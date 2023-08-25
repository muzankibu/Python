li=[]
while len(li)<5:
    a=int(input())
    if a not in li:
        li.append(a)
    else:
        continue    
print(li) 
