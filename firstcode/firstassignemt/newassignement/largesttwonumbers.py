first_largest = 0
second_largest = 0
for number in range (1, 11):
	number = int(input("Enter a number: "))
	current_number = number
	
	if first_largest < current_number:
		first_largest = current_number
		if second_largest != first_largest:
			second_largest = current_number
	

print(first_largest) 
print(second_largest)
