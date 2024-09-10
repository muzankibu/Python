def outer():
    x=10
    def inner():
        nonlocal x #try without the 'nonlocal' keyword to see the difference how both 'x' are not the same
        x=20
        print(x,  id(x))
    inner()
    print(x,  id(x))
outer()