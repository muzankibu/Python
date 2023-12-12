from functions import *
import logging
logging.basicConfig(filename='code4.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info('We are calling add function')
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
print(add(a, b))
logging.info('add function executed, task completed')
logging.info('We are calling is_even function')
d=int(input('Enter number: '))
print(is_even(d))
logging.info('is_even function executed, task completed')
logging.info('................................................')