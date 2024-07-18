print("WELCOME TO THE NUMBER FINDER FRIEND")

firstNumber = 770 
while firstNumber <= 4200:
	condition_one = firstNumber % 7 

	if condition_one == 0:
		number_divisible_by_seven = firstNumber
		if not number_divisible_by_seven % 5 == 0:
			print(f"  {firstNumber:^6}    ", end=',')
	
	firstNumber = firstNumber + 1