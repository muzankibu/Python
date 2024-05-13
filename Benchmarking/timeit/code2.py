#import timeit

from timeit import timeit
time_method1 = timeit('[i*i for i in range(1000)]', number=100000)
print(f'i*i: {time_method1} seconds')
time_method2 = timeit('[i**2 for i in range(1000)]', number=100000)
print(f'i**2: {time_method2} seconds')