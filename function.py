#prints multiples of 3 starting at 1 thru 

def print_multiples(n):
	i = 1
	output = ""
	while i <= 6:
		output += str(n*i) + "\t"
		i+=1
	print(output)

print_multiples(3)

#print_squares is a function that prints the squares of a range from (0,10)

def print_squares():
	return[n**2 for n in range(10)]

print(print_squares())

#function to find hypot of a right triangle

def hypot_triangle():
	print("type one side of the triangle")
	a = raw_input()
	print("type the second leg of the triangle")
	b = raw_input()

	hypot = (int(a)**2 + int(b)**2)**(1/2)

	print(hypot)

print(hypot_triangle())
