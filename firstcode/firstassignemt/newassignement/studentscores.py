print("Welcome to student scores evaluator")
score = 0
passed = 0
failed = 0
counter = 1

while counter <= 15:
	score = int(input("Enter a score:  "))
	if score >= 45: 
		passed = passed + 1
	elif score < 45:
		failed = failed + 1
	counter = counter + 1
print(f"{passed} passed the exam and {failed} students failed the exam")