try:
    raise NameError('It\'s a custom made message!')
except NameError as e:
    print(e)