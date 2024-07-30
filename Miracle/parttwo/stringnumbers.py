
# 1: create a function called string_numbers 
# 2: pass in two parameters, it will be of string data type
# 3: create two variables and pass these parameters to it by casting it to an integer 
# 4: create a variable called sum and add the resulting values from step 3
# 5: create a another variable to hold the string format of the sum.
# 6: cast the sum in it back to a string 
# 7: return the variable holding the string format of sum
# 8: call the function and test its inputs

def string_numbers(first_string_numbers, second_string_numbers):
	first_int_value = int(first_string_numbers)
	second_int_value = int(second_string_numbers)
		
	sum = (first_int_value + second_int_value)
	sum_in_string_format = str(sum)
	
	return sum_in_string_format



first_input = input("Enter first number in string: ")
second_input = input("Enter second number in String: ")

result = string_numbers(first_input, second_input)
print(result)