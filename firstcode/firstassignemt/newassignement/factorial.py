def factorial(number):
	total = 1
	while number >= 1:
		total = total * number
		number = number - 1
	return total

number = int(input("Enter a number to calculate its factorial:  "))

result = factorial(number)
print(result)