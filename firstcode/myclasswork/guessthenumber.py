from random import randint
print("WELCOME TO GUESS THE NUMBER GAME")

def computer():
	generated_random_number = randint(1, 1000)
	
	return generated_random_number

def game(player, computer):
	if player > computer:
		message_too_high = "too high, try again"
		return message_too_high

	elif player < computer:
		message_too_low = "too low, try again"
		return message_too_low

	elif player == computer:
		message_congrat = "Congratulation"
		return message_congrat

def get_attempt(attempt):
	if attempt < 10:
		return "you are good"
	elif attempt > 10:
		return "you can be better"
	



computer = computer()
number_of_attempt = 0

flag = ""

while(not flag == "no"):
	player = 0
	while player != computer:
		player = int(input("Guess number between 1 and 1000 with the fewest guesses:  "))
		result = game(player, computer)

		if player != computer:
			number_of_attempt = (number_of_attempt + 1)
	
		print(result)
	reward = get_attempt(number_of_attempt)
	print(reward)

	flag = input("do you want to continue? : press yes or no: \n")




