@profile
def ghuraghuri():
    count=0
    while count<=100000:
        count+=1
    return count



if __name__ == '__main__':
    temp= ghuraghuri()
    print(temp, "loops")


#for line_profiler; use 'kernprof -l -v code4.py' command in terminal (N.B: check the script path)
##for memory_profiler; use 'python -m memory_profiler code4.py' command in terminal (N.B: check the script path)
