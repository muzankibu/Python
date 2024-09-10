class Calculator:
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return abs(a-b)
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return 'can\'t be divide by zero!'
calculator1=Calculator()
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
print(calculator1.addition(a,b))
print(calculator1.subtraction(a,b))
print(calculator1.multiplication(a,b))
print(calculator1.division(a,b))
