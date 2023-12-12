from datetime import date
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)


	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person('Rana', 21)
person2 = Person.fromBirthYear('Naser', 1996)

print(person1.age)
print(person2.age)


print(Person.isAdult(22))
