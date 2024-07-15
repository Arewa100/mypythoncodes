import random

def get_name():
	player_choice = input("enter a choice rock, paper or scissors: ")
	the_computer_choice = ["rock", "paper", "scissors"]
	computer_choice = random.choice(the_computer_choice)
	choice = {"player": player_choice,"computer": computer_choice}
	
	return choice

def check_win(player, computer):
	print(f"you selected {player}, computer selected {computer}")
	if(player == computer):
		return "it is a tie"
	elif player == "rock" and computer == "scissors":
		return "you smashed computer"
	elif player == "scissors" and computer == "rock":
		return "you have been smashed"
	elif player == "scissors"  and computer == "paper":
		return "you smashed computer"
	elif player == "paper" and computer == "scissors":
		return "you were smashed"
	elif player == "paper" and computer == "rock":
		return "you smashed computer"
	elif player == "rock" and computer == "paper":
		return "you are smashed"
	else:
		return "thank you"

choices = get_name()

#result = 
check_win(choices["player"], choices["computer"])
#print(result)