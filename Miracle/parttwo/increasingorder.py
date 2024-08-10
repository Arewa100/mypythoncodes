# 1: write a function called get_sortedNumbers
# 2: pass in three parameter called num_one, num_two, num_three
# 3: inside the function, create a variable called largest, small and smallest 
# 4: compare the num_one with num_two, if num_one, compare anyone that is greater between them with num_ three
# 5: if result from step 3 equal to not zero, return "it is an odd integer"
# 6: test the function by prompting user for input


def get_sortednumbers(num_one, num_two, num_three):
	largest = 0
	small = 0
	smallest = 0
	if num_one >= num_two and num_one >= num_three: 
		largest = num_one
		if num_two > num_three:
			small = num_two
			smallest = num_three
		else:
			small = num_three
			smallest = num_two
	elif  num_two >= num_one and num_two >= num_three: 
		largest = num_two
		if num_one > num_three:
			small = num_one
			smallest = num_three
		else:
			small = num_three
			smallest = num_one
	elif  num_three >= num_one and num_three >= num_two: 
		largest = num_three
		if num_two > num_one:
			small = num_two
			smallest = num_one
		else:
			small = num_one
			smallest = num_two
		
	number_list = [smallest, small, largest]
	return number_list



result=  get_sortednumbers(5,10, 1)
print(result)




