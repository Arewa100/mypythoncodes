for count in range(1, 21):
	for newcount in range(count):
		print("*", end='')
	for counter in range(10, count, -1):
		print(" ", end='')
	for number in range(10, count, -1):
		print("*", end='')
	for num in range(1, count, 1):
		print("k", end='')
	for num in range(1, 10):
		print("*", end='')
	
	print(" ")
