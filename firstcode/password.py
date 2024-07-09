firstname = input("what is your firstname: ")
lastname = input("what is your surname: ")
age = input("how old are you: ")
age = int(age)

print("your fullname is " + firstname, lastname + " and your age is ",  age)

message = "you are responsible for your life"

if(age > 19 and age <= 45):
	print(message)

elif age >= 13 and age <= 19: 
	print("you are a teenger")  
	print("hello")

elif age > 0 and age < 13:
	print("you are still a child")
	
else: 
	print("you are old")