def dec1(darg):
    def dec2(func):
        def dec3(arg1, arg2):
            if func(arg1,arg2)==darg:
                print('True')
                return
            else:
                print('False')
        return dec3
    return dec2

@dec1(10)
def core(arg1, arg2):
    total= arg1+arg2
    return total

#result=dec1(10)(core)
#result(5,6)
core(5, 6)