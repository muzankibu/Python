class Myclass:
    def __init__(self):
        pass
    def square(self,x):
        return x**2
    @classmethod
    def cube(self,x):
        return x**3
#if __name__ == '__main':
myclass = Myclass()
print(myclass.square(3))
print(myclass.cube(3))
print(Myclass.cube(3))
print(Myclass.square(3))

