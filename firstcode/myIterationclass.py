players_name = input("Enter your name: ")
print("welcome " + players_name)

age = int(input("how old are you? " ))

if(age >= 30): 
	print("you are eligible to play the LOOPER GAME")
	select_opponent = int(input("select the number of oponent you want to play with starting between 4, 8, 16, 32: "))
	match select_opponent:
		case 4:
			opponent = ["john", "Sheun", "Olamide", "Ebuka"]
			for times in range(0, select_opponent):
				print("Your opponent is " + opponent[times])
			
		case 8:
			opponent = ["Jake", "Chris", "Olamide", "Mystery", "Folahade", "Lade", "Ade", "Micheal"]
			for times in range(0, select_opponent):
				print("Your opponent is " + opponent[times])
		case 16: 
		 	opponent = ["Jake","Chris","Olamide","Mystery","Folahade","Lade","Ade","Micheal","Olarinwa","Tobi","Ebuka","Chidima","john","Sheun","Olamide","Ebuka"]
				for times in range(0, select_opponent):
				print('Your opponent is " + opponent[times])	
		case 32: 
			print(select_opponent)
		case _:
			if(select_opponent < 4):
				print("you are out of range")
			elif(select_opponent > 32):
				print("you are out of range")
		
else:
	print("you are not eligible")
