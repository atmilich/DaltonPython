def convertScoreToGrade(n):
	grade = ""
	if(99 <= int(n) <= 100):
		print("true")
		grade = "A+"
	elif(96 <= int(n) <= 98):
		grade = "A"
	elif(93 <= int(n) <= 95):
		grade = "A-"
	elif(90 <= int(n) <= 92):
		grade = "B+"
	elif(87 <= int(n) <= 89):
		grade = "B"
	elif(84 <= int(n) <= 86):
		grade = "B-"
	elif(81 <= int(n) <= 83):
		grade = "C+"
	elif(78 <= int(n) <= 80):
		grade = "C"
	elif(75 <= int(n) <= 77):
		grade = "C-"
	elif(70 <= int(n) <= 74):
		grade = "D"
	else:
		grade = "F"
	print(grade)

#exercise 2: splits the string at the space and returns as a list, uses built in string.split function
def listOfWords(s):
	print(str(s).split())

#exercise 3: 1) isPrime returns true or false if the integer input is prime/not prime

def isPrime(n):
	j = 1

	while(j <= int(n)-1):
		import pdb
		pdb.set_trace()
		print(" ")
		j+=1
		print(j)

		if(int(n)%j == 0):
			print("False")
			return False
	
		#if(j == int(n)):
		#	print("True")

def listOfPrimes(n):
	i = 0

	while(i < int(n)):
		if(isPrime(int(n)) == True):
			print(str( isPrime(int(n))))
		i+=1

def isPalindrome(n):
	rev = n[::-1]
	if(rev == n):
		print("True")
	else:
		print("False")

def nextPalindrome(n):
	rev = n[::-1]
	while(str(n) != rev):
		n = int(n)+1
		rev = str(n)[::-1]

	print(n)

exercise = 0
print("which exercise would you like to use")
exercise = raw_input()

#asks for input to ConvertScore
if(exercise == "1"):
	print("enter the score")
	
	score = raw_input()
	convertScoreToGrade(score)

#input for listOfWords
elif(exercise == "2"):
	print("enter the sentence")
	sen = raw_input()
	listOfWords(sen)

elif(exercise == "3"):
	print("enter the number to 1. see if it is prime and 2. get the list of prime numbers until that number.")
	number = raw_input()
	isPrime(number)
	listOfPrimes(number)
#elif(exercise == "4"):
	#well spaced prime fact.

elif(exercise == "5"):
	print("enter a number to see if it's a palindrome")
	number = raw_input()
	isPalindrome(number)

elif(exercise == "6"):
	print("enter a number to find its next palindrome")
	number = raw_input()
	nextPalindrome(number)
