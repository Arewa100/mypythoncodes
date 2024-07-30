# 1: write a function called reverse
# 2: pass in one parameter called number
# 3: inside the function, seperate all numbers and create a variable called num
# 4: pass the result of step 3 to a list
# 5: iterate through the list 
# 6: while iterating multiply num by 10 and add its value to each element of the list in reverse order
# 7: step 6 is to ensure that the number is returned as a whole digit 
# 8: at the end of the function, return num
# 9: test function if its able to reverse a number

#  writing for palindrome

# 1: write a function called reverse
# 2: pass in one parameter called number
# 3: inside the function, seperate all numbers and create a variable called num
# 4: pass the result of step 3 to a list
# 5: iterate through the list 
# 6: while iterating multiply num by 10 and add its value to each element of the list in reverse order
# 7: step 6 is to ensure that the number is returned as a whole digit 
# 8: compare num with the input number if it is equal to each other, return "number is palindome" 
# 9: if it is not equal to each other, return "number is not palindome"
# 9: test function if its able to reverse a number



def reverse(number):  
	num = 0
	third_number = number % 10       
	first_division = number // 10     
	second_number = first_division % 10         
	first_number = first_division // 10   
	
	number_list = [first_number, second_number, third_number] 
	
	for count in range(1, len(number_list)+1):
		num = num * 10 + number_list[-count]
	return num


def is_palindrome(number):  
	num = 0
	third_number = number % 10       
	first_division = number // 10     
	second_number = first_division % 10         
	first_number = first_division // 10   
	
	number_list = [first_number, second_number, third_number] 
	
	for count in range(1, len(number_list)+1):
		num = num * 10 + number_list[-count]
	if num == number:
		return "number is palindome"
	else:
		return "number is not palindome"

result_one =  reverse(434)
print(result_one)

result_two = is_palindrome(result_one)
print(result_two)
