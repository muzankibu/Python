import re

pattern = 'a{4,5}'
test_string = 'ab aab baa'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	
