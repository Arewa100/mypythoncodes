name = input("what is your name: ")
print("welcome to BOUNTY BANK " + name)

sentinel = ''
balance = 0

while(sentinel != 'E'):
	
	sentinel = input("Enter 'D'deposit, 'W' to withdraw OR 'E' to show balance: ")
	match sentinel:
		case 'D':
			deposit = int(input("enter amount to deposit: "))
			balance	= balance + deposit

		case 'W':
			withdraw = int(input("enter amount to withdraw: "))
			balance = (balance - withdraw)

print("your balance is ", balance, name)

