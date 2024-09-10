def decortor(x):
    def wrapper(fuct, a, b):
        if fuct(a,b) == x:
            print('True')
        else:
            print('False')
        return
    return wrapper

def core(a,b):
    return a+b


decortor(10)(core, 5, 6)
