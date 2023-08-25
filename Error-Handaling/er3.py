try:
    myfile=open('test.txt')
    con=myfile.read()
    i=int(con.strip())
except IOError as e:
    errno, strerror=e.args
    print('I/O error({0}): {1}'.format(errno,strerror))
except ValueError:
    print('No valid integer in line')
except:
    print('Unexpected error!')