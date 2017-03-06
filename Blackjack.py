import numpy
import math
from random import randint

#code for Blackjack
#Author: Aly Milich, Feb. 2017
#Includes 2 modes, practice and play
#Uses a 2D array that represents all of the possible cards in a deck and randomly selects one when the user chooses to "hit"

cards = numpy.zeros((13,4)) #declaring a 2D array

#filling the array. the entire 0th row = 2, 1st row = 3, etc.
cards[0,:] = 2
cards[1,:] = 3
cards[2,:] = 4
cards[3,:] = 5
cards[4,:] = 6
cards[5,:] = 7
cards[6,:] = 8
cards[7,:] = 9
cards[8,:] = 10
cards[9,:] = 10 #jacks
cards[10,:] = 10 #queens
cards[11,:] = 10 #kings
cards[12,:] = 11 #aces

sumcard, dealersum = 0, 0

print("practice or play?")
mode = raw_input()

#practice mode
if(mode == "practice"):
	action = "hit" #start off action has to be hit

	#hit: randomly select a card from the array and then change that to 0 (so it can't be reselected)
	#if the card selected is already 0, reselect
	while(action == "hit"):
		randrow = randint(0,12)
		randcol = randint(0,3)

		if cards[randrow][randcol]==0:
			randrow = randint(0,12)
			randcol = randint(0,3)
			
		lastcard = cards[randrow][randcol]
		cards[randrow][randcol] = 0

		sumcard += lastcard #increment sum
		
		#translating the face cards so output makes sense
		if(randrow == 9):
			print("last card chosen: Jack (counted as 10)")

		elif(randrow == 10):
			print("last card chosen: Queen (counted as 10)")

		elif(randrow == 11):
			print("last card chosen: King (counted as 10)")

		elif(randrow == 12):
			print("last card chosen: Ace (counted as 11)")

		else:
			print("last card chosen: " + str(lastcard))

		print("sum: " + str(sumcard))
		print("   ")	
	
		if(sumcard == 21):
			print("you win!")
			break	

		if(sumcard > 21):
			print("you lose")
			break

		print("hit or stay?")
		action = raw_input()

#play mode (against dealer)
if(mode == "play"):
	action = "hit"

	while(action == "hit"):
		#selecting player card (same way as before, choose card from array and change it to 0)
		randrow = randint(0,12)
		randcol = randint(0,3)

		if(cards[randrow][randcol]==0):
			randrow = randint(0,12)
			randcol = randint(0,3)

		lastcard = cards[randrow][randcol]
		cards[randrow][randcol] = 0
		sumcard += lastcard

		#dealer card -- selected the same way as player card
		dealrow = randint(0,12)
		dealcol = randint(0,3)

		if(cards[dealrow][dealcol] ==0):
			dealrow = randint(0,12)
			dealcol = randint(0,3)
				
		dealerlast = cards[dealrow][dealcol]
		cards[dealrow][dealcol] = 0
		dealersum += dealerlast
		
		#translating face card output for player and dealer
		if(randrow == 9):
			print("last card: Jack (counted as 10)")
	
		elif(randrow == 10):
			print("last card: Queen (counted as 10)")
		
		elif(randrow == 11):
			print("last card: King (counted as 10)")

		elif(randrow == 12):
			print("last card: Ace (counted as 11)")

		else:
			print("last card: " + str(lastcard))

		print("your sum: " + str(sumcard)) #player's sum
		
		if(dealrow == 9):
			print("dealer's last card: Jack (counted as 10)")

		elif(dealrow == 10):
			print("dealer's last card: Queen (counted as 10)")

		elif(dealrow == 11):
			print("dealer's last card: King (counted as 10)")

		elif(dealrow == 12):
			print("dealer's last card: Ace (counted as 11)")

		else:
			print("dealer's last card: " +  str(dealerlast))

		print("dealer's sum: " + str(dealersum)) #dealer's sum
		print("   ") #space in between 
	
		#if the player's sum goes over 21 while dealer is under 21 player loses
		if(sumcard > 21 and dealersum < 21):
			print("dealer wins")
			break
		
		#vice versa. if the dealer's sum is over 21 while the player is under
		elif(dealersum > 21 and sumcard < 21):
			print("dealer is out, you win.")
			break

		#if they're both over 21, see which has a smaller difference 
		elif(dealersum > 21 and sumcard > 21):
			diff = sumcard -21
			dealerdiff = dealersum-21

			if(dealerdiff > diff):
				print("you win")
				break

			elif(diff > dealerdiff):
				print("dealer wins")
				break

		#if the dealer hits 21 wins
		elif(dealersum == 21):
			print("dealer wins")

		#if the player hits 21 wins
		elif(sumcard == 21):
			print("you win")
	
				#if dealersum + sumcard < 17
		if(sumcard + dealersum > 17):
			print("hit or stay?")
			action = raw_input()
	
	#if the player choses stay, calculate differences and see which is smaller (who wins)
	while(action == "stay"):
		diff = 21-sumcard
		dealerdiff = 21-dealersum
		
		if(dealerdiff > diff):
			print("you win")
			break

		elif(diff > dealerdiff):
			print("dealer wins")
			break
		
		else: #if dealer and player sum are equal
			print("tie")
			break
