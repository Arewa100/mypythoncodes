import math
def divide_or_square(number):
	if number % 5 == 0:
		return math.sqrt(number)
	elif number % 5 != 0:
		return number % 5 

number = int(input("Enter a number:  "))
result = divide_or_square(number)
print(result)