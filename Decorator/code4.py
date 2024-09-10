class Myclass:
    def addition(self,x,y):
        return x+y
    @staticmethod
    def multiplication(x,y):
        return x*y
obj=Myclass()
print("Addition of 2 numbers:", obj.addition(10,5)) #calling the method using object name and passing arguments to it
print("Multiplication of 2 numbers:", Myclass.multiplication(3,4))
#print("Multiplication of 2 numbers:", Myclass.addition(3,4)) ---> #cant access addition() by Myclass.addition as it is not @staticmethod neither @classmethod 