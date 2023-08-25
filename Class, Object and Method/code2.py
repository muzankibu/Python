class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a-self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        try:
            return self.a/self.b
        except ZeroDivisionError:
            return 'Impossible to perform!'
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
mycal=Calculator(a,b)
print(mycal.addition())
print(mycal.subtraction())
print(mycal.multiplication())
print(mycal.division())