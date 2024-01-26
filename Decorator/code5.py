def taker(darg):
    def ftaker(func):
        def wrapper(arg):
            print('function arg:', arg)
            print('decorator arg:', darg)
            func(arg)
        return wrapper
    return ftaker

@taker(10)
def callerm(targ):
    print(targ)

callerm(5)