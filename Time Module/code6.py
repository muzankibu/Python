#strftime
import time

t=time.gmtime()
print(t)
print(time.strftime('%I:%M:%S %p %d %B, %Y'))
