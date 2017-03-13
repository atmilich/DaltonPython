
#print("enter the number of rows")
#rows = raw_input

#print("enter the number of columns")
#columns = raw_input

a = [[1, 4, 6]]
b = [[2, 3], [5, 8], [7, 9]]

def mmult(a, b):
	n1 = len(a)
	m1 = len(a[0])
	n2 = len(b)
	m2 = len(b[0])

	c = [[0]*m2]*n1

	if m1 != n2:
		print "columns of first must equal rows of second"
		return

	else:
		for i in range(n1):
			for j in range(m2):
				#take a dot product
				for k in range(m1):
					#dotsum += a[i][k] + b[k][j]
					c[i][j] += a[i][k] * b[k][j]

	return c

print(mmult(a,b))

x = [1,2]
y = [3,4]

def dot(x,y):
	dotsum = 0
	for i in range(len(x)):
		dotsum = dotsum + x[i]*y[i]
	
	print dotsum
	return dotsum
