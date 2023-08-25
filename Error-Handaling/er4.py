try:
    myfile=open('test.txt')
    con=myfile.read()
    i=int(con.strip())
except(IOError, ValueError):
    print('There must be some error!')