class Point:
	pass #python's equivalent of return "" -- makes the code work but doesn't return anything yet

	def _init_(self, x = 0, y = 0): #defines class implicitly, need _init_(self and then you can change it as needed
		self.x = x
		self.y = y

	def distance_from_origin(self):
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Point()
p.x = 5
p.y = 12

print(str(p.distance_from_origin()))
