import time

start= time.clock()
count=0
while count<=50000:
    print(count)
    count+=1
stop=time.clock()
print('Computational Cost:', stop-start)