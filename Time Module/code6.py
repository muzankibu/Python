#strftime
import time

t=time.gmtime()
print(time.strftime('%I:%M:%S %p %d %B, %Y', t))
