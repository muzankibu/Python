import re
str='abbbbba'
ptr='a.{2,3}a'
result=re.findall(ptr,str)
print(result)