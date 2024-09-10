def add(a,b):
    return a + b
def is_even(number):
    if (number%2)==0:
        return True
    else:
        return False


if __name__ == '__main__':

    print(add(10,2))
    print(is_even(1))
    print('File executed from: ', __name__)
