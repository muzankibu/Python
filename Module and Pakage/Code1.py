def fib(n):
    series = []
    a,b=0,1
    while b<n:
        series.append(a)
        a,b=b,a+b
    return series
if __name__ == '__main__':
    temp=fib(100)
    print(temp)