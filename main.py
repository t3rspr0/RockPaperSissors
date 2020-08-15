#This is a Miguel Ferreira production

'''
	Changes by João Pedro

	##### Updates #####
	1. Neural Network to learn how player plays the game. ||| Lines: (17, 40, 93-131)
	2. New function to get user most used option. ||| Lines: (41-65)
	3. A while True to never end the game in one competition. ||| Line: (71)
	4. A KeyboardInterrupt except block and leaving system. ||| Lines: (18, 72-82)
	5. Prints changes. ||| Lines: (72, 74, 136-148)
'''

import random #this is an important, I hope you like him, 'cause he'll be helping the computer to choose a random string so the computer can play
import os

options = ['rock', 'paper', 'scissors'] #just a list, where the computer can check is choice
userlasts = [] # A list that holds all the user selected options, this way the computer can learn how player plays and his most used options
wannaleave = False

# ==== Game functions ==== #

def check_winner(player, computer): #this is a kind thing called "function" and it will recieve 2 values --> the player choice and the computer choice
	#in this line below me (yes, I'm the comment) we set this variable as false, so we can return them anyways
	win = False

	#this following lines are just the game logic with some if's in the middle (as you can see, there's no cheating in this game) 
	if player == "rock":
		if computer == "scissors":
			win = True
	elif player == "paper":
		if computer == "rock":
			win = True
	else: #this can just be scissors, as we did the validation before
		if computer == "paper":
			win = True

	#see, we return them here
	return win

def get_most_used_option(): # Function that gets the most used option
	times = [0, 0, 0] # Holds 3 values that will be update relative to the user most used options.
	#print(userlasts)

	# Searchs for all the options inside userlasts and add 1 to the own index in the times list.
	for option in userlasts:
		if option == 'rock':
			times[0] += 1
		elif option == 'paper':
			times[1] += 1
		elif option == 'scissors':
			times[2] += 1

	# If rock is the bigger one
	if times[0] > times[1] and times[0] > times[2]:
		return 'rock'
	# If paper is the bigger one
	elif times[1] > times[0] and times[1] > times[2]:
		return 'paper'
	# If scissors is the bigger one
	elif times[2] > times[1] and times[2] > times[1]:
		return 'scissors'
	# If all the indexes have the same int
	else:
		return None 

# ====================== #

# ==== Main program ==== #

while True:
	print('\nRock, Paper or Scissors?')
	try:
		player = str(input("!>> ")).lower() #here we put .lower() so we can transform "Rock" in just "rock"
	except KeyboardInterrupt: 
		if wannaleave:
			exit()
		else:
			wannaleave = True
			print('\nCtrl^C again to exit the program, or just type anything to break the operation.')
			continue

	wannaleave = False

	# Adds shortcuts using the first letter of each word.
	if player == 'r':
		player = 'rock'
	elif player == 'p':
		player = 'paper'
	elif player == 's':
		player = 'scissors'

	if player in options: #in this cute and tiny line, we'll check if the... well... thing that the player chose is in the array (check the final of the code for more)
		userlasts.append(player) # Appends the option in the userlasts list.
		mostone = get_most_used_option() # Gets the most used option
		rand = random.randint(0, 100) # Generates a random number

		# Has a big chance that the player will trow rock again or the rock defeater next time.
		if mostone == 'rock':
			# Will chose paper to try win the rock, but only if random reachs 85 to 90
			if rand >= 85 and rand < 90:
				computer = options[1]
			# Otherwise rand bigger than 90, it will chose rock to try draw the game.
			elif rand > 90:
				computer = options[0]
			# Else if rand is lower than 85 it will chose a random option to use.
			else:
				computer = random.choice(options) # Tells the computer to choice randomly
		# Has a big chance that the player will trow paper again or the paper defeater next time.
		elif mostone == 'paper':
			# Will chose scissors to try win the paper, but only if random reachs 85 to 90
			if rand >= 85 and rand < 90:
				computer = options[2]
			# Otherwise rand bigger than 90, it will chose paper to try draw the game.
			elif rand > 90:
				computer = options[1]
			# Else if rand is lower than 85 it will chose a random option to use.
			else:
				computer = random.choice(options) # Tells the computer to choice randomly
		# Has a big chance that the player will trow paper again or the paper defeater next time.
		elif mostone == 'scissors':
			# Will chose rock to try win the scissors, but only if random reachs 85 to 90
			if rand >= 85 and rand < 90:
				computer = options[2]
			# Otherwise rand bigger than 90, it will chose scissors to try draw the game.
			elif rand > 90:
				computer = options[1]
			# Else if rand is lower than 85 it will chose a random option to use.
			else:
				computer = random.choice(options) # Tells the computer to choice randomly
		else:
			computer = random.choice(options) # Tells the computer to choice randomly

		#print(computer) #just for debbuging pourposes, you can delete it later

		if player == computer:
			os.system('cls' if os.name != 'NT' else 'clear')
			print(f'\nThe competition was {player} vs {computer}. It was a draw!')
		else:
			check_winner(player, computer)
			if check_winner(player, computer): #check the end of the code, again...
				#Player wins!!!!
				os.system('cls' if os.name != 'NT' else 'clear')
				print(f'\nThe competition was {player} vs {computer}. You win!')
			else:
				#Well, the computer was lucky -_-
				os.system('cls' if os.name != 'NT' else 'clear')
				print(f'\nThe competition was {player} vs {computer}. Computer won the game!')
	else:
		continue


'''

if player in options:
	print("Stuff")

is kinda the same thing as:


if player == "rock" or player == ""paper" or player == "scissors":
	print("Stuff")

but we need to use everything the language gives us


-------------------------------------------------------------------

if check_winner(player, computer):
	{condition}

is the same as:

if check_winner(player, computer) == True:
	{condition} ---> in this case, the player would win


'''

