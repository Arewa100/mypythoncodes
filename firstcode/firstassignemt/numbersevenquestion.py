number_given = 1024
second_number_given = 10

first_multiple = (number_given % 4)
second_multiple = (second_number_given % 2)

if(first_multiple == 0):
	print(number_given, "is a multiple of 4")
if(second_multiple == 0):
	print(second_number_given, "is a multiple of 2")