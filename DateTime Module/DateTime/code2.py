from datetime import datetime

temp='11:50:20 AM 27 January, 2000'
print(datetime.strptime(temp, '%I:%M:%S %p %d %B, %Y'))

t=datetime.now()
print(t.strftime('%I:%M:%S %p %d %B, %Y'))