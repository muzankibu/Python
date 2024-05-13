import timeit
#import time
def functionA():
   print("Function A starts the execution.............")
   print("Function A completes the execution!")
def functionB():
   print("Function B starts the execution.............")
   print("Function B completes the execution!")
start_time = timeit.default_timer()
functionA()
print('Time taken by Function A:',timeit.default_timer() - start_time)
print('\n\n')
start_time = timeit.default_timer()
functionB()
print('Time taken by Function A:',timeit.default_timer() - start_time)