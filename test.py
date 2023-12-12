import re

txt = "hello planet"

#Check if the string ends with 'planet'

x = re.findall("Planet$", txt)
if x:
  print("Match")
else:
  print("No match")
