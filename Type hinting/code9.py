from typing import NewType

# Define a type alias for a string representing a person's name
PersonName = NewType('PersonName', str)

# Use the type alias in function parameters
def greet_person(name: PersonName) -> str:
    return f"Hello, {name}!"

# Usage
#name1 = PersonName("Alice")
name2 = PersonName("Bob")

print(greet_person('Alice'))  
print(greet_person(name2))

#use mypy for understanding