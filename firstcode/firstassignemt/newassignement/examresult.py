passes = 0
failure = 0

user_input = 0;
print(type(user_input))

while not user_input == -1:
	user_input = int(input("enter result (1 for pass:  2 for failure): "))
	if(user_input == 1):
		passes += 1
	elif not user_input ==  -1:
		failure += 1
print(f"the number of passes is {passes} and the number failures is {failure}")