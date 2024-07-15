def palindrome(number):
	
	first_division = (number // 10)

	fifth_number = (number % 10)

	fourth_number = (first_division % 10) 

	second_division = (first_division // 10)
	third_number = (second_division % 10) 

	third_division = (second_division // 10)
	second_number = (third_division % 10)

	fouth_division = (third_division // 10)
	first_number = (fouth_division)
	
	if first_number == fifth_number and second_number == fourth_number: 
		
		message = "number is palindrome"
		
		return message
	else:
		message = "number is not palinrome"
		return message

for counter in range(10):
	number = int(input("Enter a number to check if it is palindrome:  "))
	result = palindrome(number)
	print(result)


