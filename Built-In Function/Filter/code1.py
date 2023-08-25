def div(x):
    if x%2==0:
        return True
    else:
        return False
li=[1,2,3,4,5]
main_list=filter(div,li)
print(list(main_list))