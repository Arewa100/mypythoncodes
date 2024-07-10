first_number  = float(input("Enter first number: "))
second_number  = float(input("Enter second number: "))
third_number  = float(input("Enter third number: "))

if(first_number > second_number and second_number > third_number):
	print(third_number, second_number, first_number)

elif(first_number < second_number and second_number < third_number):
	print(first_number, second_number, third_number)

elif(second_number > first_number and first_number > third_number):
	print(third_number, first_number, second_number)

elif(third_number > first_number and first_number > second_number):
	print(second_number, first_number, third_number)

elif(second_number < first_number and third_number < first_number):
	print(second_number, first_number, third_number)