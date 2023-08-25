list=[1,2,3,4,5,6,7,8,9,10]
a=int(input("Enter number:"))
count=0
for i in list:
    if i==a:
        count=count+1
        print(f"{a}"+" is there & found after"+f" {count}"+"cycle")
        break
    else:
        continue
else:
    print(f"{a}"+" isnt there")