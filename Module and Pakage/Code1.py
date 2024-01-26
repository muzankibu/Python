def fib(n):
    series = []
    a,b=0,1
    while b<n:
        series.append(a)
        a,b=b,a+b
    return series

print('File executed from:', __name__)
if __name__ == '__main__':
    temp=fib(100)
    print(temp)