def taker(darg):
    def ftaker(func):
        def wrapper(arg):
            print('function arg:', arg)
            print('decorator arg:', darg)
            func(arg)
        return wrapper
    return ftaker

#@taker(10)
def callerm(targ):
    print(targ)

callerm = taker(10)(callerm)

# Call the decorated function callerm with the argument 100
callerm(100)
