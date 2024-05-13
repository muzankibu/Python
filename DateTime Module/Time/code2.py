from datetime import time

t=time(9,10,55)
print(t.strftime('%I:%M:%S'))
print(t.replace(10,20,32))