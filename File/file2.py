def words(lines):
    count=0
    words=lines.split()
    for item in words:
            count+=1
    print('Number of words:',count)

def letters(lines):
    count=0
    for item in lines:
        if item==' ':
            pass
        else:
            count+=1
    print('Number of letters:',count)

data=open('tt.txt', 'r')
lines=data.read()
print('File contents--\n',end='')
print(lines)
count=0
for item in lines:
    count+=1
print('\nNumber of lines:',count)
words(lines)
letters(lines)