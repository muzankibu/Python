import re
mystr= 'Naruto is better MC but One Piece is better anime. Hail Naruto, Hail One Piece'
print(re.findall('One Piece', mystr))
print(re.search('Naruto', mystr))
print(re.match('One Piece', mystr))
if re.search('but', mystr):
    print("Yes")

