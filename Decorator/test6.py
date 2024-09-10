def taker(func):
    def taker2(a,b):
        print('Hi')
        func(a,b)
        print('Bye')
    return taker2
@taker #
def giver(a,b):
    print('Sum:', a+b)


##result=taker(giver)
##result(2,2)
giver(2,2) #