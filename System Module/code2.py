import sys

try:
    print(1/0)
except ZeroDivisionError:
    print(sys.exc_info())