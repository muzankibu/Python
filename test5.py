n=int(input())
s=0
if n%2!=0:
   for i in range(1,n+1,2):
      s=s+i
      if i==n:
         print(i,end='=')
      else:
         print(i,end='+')

   print(s)
else:
   for i in range(1,n+1,2):
         s=s+i
         if i==(n-1):
            print(i,end='=')
         else:
            print(i,end='+')

   print(s)     