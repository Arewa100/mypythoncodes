#pseudo code

# 1: write a function called check_even_numbers
# 2: pass in one parameter called counter
# 3: create a variable called value and assign value 0 to it 
# 4: create a list and pass each value seperated into as list element
# 5: iterate through the list and check if each element divided by 2 is equal to zero
# 6: if it is True increment value variable
# 7: check if value is equals to 4, if true return True
# 8: if false return False

#  outside the function

# 9: create a variable called counter and assign a value of 1000 to it.
# 10: write a iteration statement 
# 11: give it a condition starting from counter and ending in 3000 
# 12: create a variable amd assign it to the modulo of counter and 2
# 13: write a condition statement using if statement
# 14: if the condition in number 4 is equal to zero, call the function created and pass counter to it
# 15: if function returns True, print the counter 
# 16: increment counter and repeat the statements until condition evalutes to False




def check_even_numbers(counter):
	value = 0
	fourthnumber = counter % 10
	firstdivision = counter // 10  
	thirdnumber = firstdivision % 10  
	seconddivision = firstdivision // 10    
	secondnumber = seconddivision % 10     
	firstnumber = seconddivision // 10  
		
	number_list = [firstnumber, secondnumber, thirdnumber, fourthnumber]
		
	for count in number_list:
		if count % 2 == 0:
			value = value + 1
	if value == 4:
		return True
	else:
		return False



counter = 1000

while counter <= 3000:
	result = (counter % 2)
	if result == 0:
		feedback = check_even_numbers(counter)
		if feedback == True:
			print(f"{counter }", end= ',  ')
	
	counter = counter + 1