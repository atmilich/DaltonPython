alist = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]

#iteratively
def binarySearchIt(alist, item):
	first = 0
	last = len(alist)-1
	found = False
	while first <= last and not found:
		midpoint = (first + last)/2
		if(alist[midpoint] == item):
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found

#recursively
def binarySearchRecur(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist)/2
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return binarySearchRecur(alist[:midpoint], item)
			else:
				return binarySearchRecur(alist[midpoint+1:],item)

print(binarySearchIt(alist, 55))

print(binarySearchRecur(alist, 55))
