from time import time
def timer(any_function):
    #def count_time():
        start = time()
        any_function()
        stop = time()
        print("\nTime taken: ",((stop-start)*10),'seconds')
        #return
    #return count_time()
@timer
def hello():
    print("Hello World!",end=' ')
@timer
def another_function():
    for item in range(1,100):
        print(item,end=' ')