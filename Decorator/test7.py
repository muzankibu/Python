def taker(func,x,y):
    func(x,y)
#@taker
def giver(a,b):
    print('Sum:', a+b)


taker(giver,2,2)

#giver(2,2)