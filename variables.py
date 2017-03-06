#boolean values are capitalized -- True and False
#there are three logic operators -- and, or, and not. (typed out)
#conditionals -- if, elif, else

action = "hit"

x = 16

if x > 16:
	action = "stay"
elif x == 16:
	print("hit or stay")
	action = raw_input()

else:
	action = "hit"

print(action)
