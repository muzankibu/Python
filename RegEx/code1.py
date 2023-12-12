import re
mystr='purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
temp= mystr.split(',')
print(temp)
for phrase in temp:
    result= re.search("([\w\.-]+)@([\w\.-]+)", phrase)
    print(result.group())