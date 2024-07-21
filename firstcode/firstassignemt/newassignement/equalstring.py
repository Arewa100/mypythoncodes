def equal_string(first_string, second_string):
	reversed = ''

	if len(first_string) == len(second_string):
		iterable_list = list(first_string)
		for count in iterable_list:
			if count in second_string:
				reversed = reversed + count
			else:
				reversed = ''
		if len(first_string) == len(reversed):
			return True
		else: 
			return False
	else:
		return False
	

result = equal_string("love", "evol")
print(result)

