from profilehooks import profile

@profile #similer to cProfile module
def ghuraghuri():
    count=0
    while count<=100000:
        count+=1
    return count



if __name__ == '__main__':
    temp= ghuraghuri()
    print(temp, "loops")

