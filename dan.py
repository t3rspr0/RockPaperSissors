#This is a Miguel Ferreira production

import random #this is an important, I hope you like him, 'cause he'll be helping the computer to choose a random string so the computer can play

options = ['rock','paper','scissors'] #just a list, where the computer can check is choice


# ==== Game function ==== #

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

# ====================== #

# ==== Main program ==== #

print("=== Rock, paper, scissors... ===\n")

player = str(input("Rock, paper, scissors...? » ")).lower() #here we put .lower() so we can transform "RoCk" in just "rock"

if player in options: #in this cute and tiny line, we'll check if the... well... thing that the player chose is in the array (check the final of the code for more)
	computer = random.choice(options) #select the computer choice randomly

	#print(computer) #just for debbuging pourposes, you can delete it later

	if player == computer:
		print("\n=== Draw ====")
	else:
		check_winner(player, computer)
		if check_winner(player, computer): #check the end of the code, again...
			#Player wins!!!!
			print("\n==== You won the computer!! ====")
		else:
			#Well, the computer wass lucky -_-
			print("\n==== You lost :( try again!! ====")
else:
	while player not in options:
		player = str(input("Rock, paper, scissors...? » ")).lower() #here we put .lower() so we can transform "RoCk" in just "rock"

		if player in options: #in this cute and tiny line, we'll check if the... well... thing that the player chose is in the array (check the final of the code for more)
			computer = random.choice(options) #select the computer choice randomly

			if player == computer:
				print("\n==== Draw ====")
			else:
				check_winner(player, computer)
				if check_winner(player, computer): #check the end of the code, again...
					#Player wins!!!!
					print("\n==== You won the computer!! ====")
				else:
					#Well, the computer wass lucky -_-
					print("\n==== You lost :( try again!! ====")


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


