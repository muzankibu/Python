def print_int(number):
    def get_int_ass_str(number):
        return str(number)
    x=get_int_ass_str(number)
    return x
print(print_int(130))
print('................................')
def print_int(number):
    def get_int_ass_str(number):
        return str(number)
    return get_int_ass_str(number)
    
print(print_int(130))