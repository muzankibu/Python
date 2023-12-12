import logging
logging.basicConfig(filename='code2.log', level=logging.INFO)
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
try:
    temp=a/b
    print(temp)
except ZeroDivisionError as e:
    logging.exception("Divided by zero error")
