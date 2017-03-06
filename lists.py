listdemo = [1, 2.0, "three", (2**2), [5, 6]] #elements do not have to be of the same type

emptylist = [] #length 0 empty list

print(len(listdemo))
print(len(emptylist))
print("the fifth element is " + str(listdemo[4]))

print(listdemo[0])

del listdemo[0]

print(listdemo[0])

#the element [0] is always going to be 0 (can't refer to it as anything besides that) but you can loop around in the positive and negative direction

print("-1" + str(listdemo[-1])) #loops around

emptylist.append("hi my name is") #adding something to a list
superlist = emptylist + listdemo #concatinating 2 lists

i=0
while(i < len(superlist)):
	print(str(i) + str(superlist[i]))
	i+=1

print(superlist)

