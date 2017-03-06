name = "josh"

length = len(name)

last = name[length-1]

print(length)
print(last)

first = name[0]
pigname = name[1:] + first + "ay"

print(pigname)

s = "ginzberg, moretti, campbell"    #example of string slices
print(s[0:8], s[10:17], s[19:27])

#taking in input
print("type a word to see in pig latin")
myword = raw_input()
pigword = myword[1:] + myword[0] + "ay"

for char in pigword:
	print char
