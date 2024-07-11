name = input("Enter your name: ")
print("welcome to the grade checker " + name)

grade = int(input("Enter you grade " + name + ": "))

if(grade >= 75):
	print("your grade is A " + name)
elif(grade >= 65):
	print("your grade is B " + name)
elif(grade >= 50):
	print("your grade is C " + name)
elif(grade >= 40):
	print("your grade is D " + name)
else:
	print("your grade is F " + name + "," + " work on yourself")	