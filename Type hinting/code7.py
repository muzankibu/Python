import typing

names: typing.List[str] = ['Nazu', 'Rana', 'Rahim The Basha Bhai', 'Bappi the lip sync', '123', '144']
print(names)

fees: typing.Dict[str, int] = {
    'java': 2355,
    'spring boot': 232454,
    'django': 123
                               }
print(fees)

def convert(value: int)-> int:
    value = value.upper()
    return value
print(convert('Showrav')) #<-wrong typed value was giver by the user