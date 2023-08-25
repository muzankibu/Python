#method overriding
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
class Supercalculator(Calculator):
    def addition(self,a,b,c):
        return a+b+c
    def square(self,a,b):
        return a*a,b*b
    def cube(self,a,b):
        return a*a*a,b*b*b
cal1=Supercalculator()
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=int(input('Enter 3rd number:'))
print(cal1.addition(a,b,c))
print(cal1.subtraction(a,b))
print(cal1.multiplication(a,b))
print(cal1.division(a,b))
print(cal1.square(a,b))
print(cal1.cube(a,b))