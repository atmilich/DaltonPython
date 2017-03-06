class Dog(object):
	def _init_(self, breed, fur, eyes, age):
		self.breed = breed
		self.fur = fur
		self.eyes = eyes
		self.age = age

def toHumanYears(y):
	dogYears = int(y)*7
	return dogYears

rex = Dog()
rex.breed = "pug"
rex.fur = "white"
rex.eyes = "brown"
rex.age = 11

print(toHumanYears(rex.age))
