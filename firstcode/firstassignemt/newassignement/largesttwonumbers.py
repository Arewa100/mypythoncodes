first_largest = 0
second_largest = 0
for number in range (1, 11):
	number = int(input("Enter a number: "))
	current_number = number
	
	if first_largest < current_number:
		first_largest = current_number
	elif second_largest < number or current_number < number:
		second_largest = number	

print(first_largest) 
print(second_largest)
