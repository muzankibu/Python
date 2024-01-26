import time

start= time.time()
count=0
while count<=50000:
    print(count)
    count+=1
stop=time.time()
print('Computational Cost:', stop-start)