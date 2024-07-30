# 1: write a function called check_numbers
# 2: pass in one parameter called numbers
# 3: inside the function, divide number by 2, store its result 
# 4: if result from step 3 equal to zero, return "it is an even integer"
# 5: if result from step 3 equal to not zero, return "it is an odd integer"
# 6: test the function by prompting user for input


def check_numbers(numbers):
	if number % 2 == 0:
		return "it is an even integer"
	else:
		return "it is an odd integer"


number = int(input("Enter a number:  "))
result = check_numbers(number)
print(result)