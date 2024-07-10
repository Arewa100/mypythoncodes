print("welcome friend. We want to determine if a number is odd of even\n")
number = input("Enter any number: ")
number = int(number)

result = (number % 2)
if(result == 0):
	print(number, "is an even number")
else:
	print(number, "is an odd number")