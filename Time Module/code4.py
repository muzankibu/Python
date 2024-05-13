import time

start= time.perf_counter()
count=0
while count<=50000:
    print(count)
    count+=1
stop=time.perf_counter()
print('Computational Cost: %.2f' %(stop-start))