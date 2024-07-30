# 1: write a function called reverse
# 2: pass in one parameter called number
# 3: inside the function, seperate all numbers 
# 4: pass the result of step 3 to a list
# 5: if result from step 3 equal to not zero, return "it is an odd integer"
# 6: test the function by prompting user for input


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

result =  reverse(234)
print(result)
