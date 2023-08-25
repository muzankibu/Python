class Customerror(Exception):
    def __init__(self,message):
        self.message = message
try:
    raise Customerror('It is a custom error.')
except Customerror as e:
    print (e)