#The finally block gets executed no matter if the try block raises any errors or not:
try:
    print(5)
except:
    print("Something went wrong")
else:
    print("This is else block")
finally:
    print("The 'try except' is finished")
