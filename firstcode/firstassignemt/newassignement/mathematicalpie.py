number = 4
pi = 0
terms = 0
for count in range(1, 5):
	if count % 2 == 1:
		terms = number/count
	elif count % 2 == 0:
		terms = -(number/count)
	pi = pi + terms
	print(pi)
	
	
		
		
	
	 
	