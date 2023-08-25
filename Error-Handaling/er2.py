try:
    with open('test.txt','r') as myfile:
        con=myfile.read()
        print(con)
except FileNotFoundError:
    print('File does not exits!')

try:
    myfile=[1,2]
    print(myfile[5])
except IndexError as a:
    print(a)
