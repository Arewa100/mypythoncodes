def average(number, *numbers):
	value = (number,)
	sum_of_length = len(numbers) + len(value)

	sum = 0
	for count in numbers:
		sum = sum + count
	total_sum = sum + number
	quotient = total_sum / sum_of_length
	return quotient

result = average(30)
print(result)	