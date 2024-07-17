import random
name = input("WELCOME FRIEND WHAT IS YOUR NAME: ")
print("welcome " + name)
	
def arithmeticproblems():
	list_of_problems = ["solve for x in 2x + 2 = 0", "Look at this series: 22, 21, 23, 22, 24, 23, What number should come next?", "Look at this series: 53, 53, 40, 40, 27, 27, What number should come next?", "60 Times of 8 Equals to?", "What is the Next Prime Number after 7?", "The Product of 131 x 0 x 300 x 4", "Solve: 3 + 6 x (5 + 4) / 3 - 7", "Solve: 23 + 3 / 2", "What is 6% Equals to", "How Many Years are there in a Decade?", "How Many Months Make a Century?", "How Many Sides are there in a Decagon?", "27 is a perfect cube. If true then what is the perfect cube of 27?", "Look at this series: 36, 34, 30, 28, 22 What number should come to fill in the blank space", "What is the sum of 130+125+191?", "Find the missing terms in multiple of 3: 3, 6, 9, __, 15", "Solve: 300 – (150 x 2)", "What is the next prime number after 5?"]
	the_random_questions = random.choice(list_of_problems)
	return the_random_questions

def grade(attempt, question):
	if question == "solve for x in 2x + 2 = 0" :
		if attempt == 1:
			return "passed"
		else:
			return "failed"
	elif question == "Look at this series: 22, 21, 23, 22, 24, 23, What number should come next?":
		if attempt == 25:
			return "passed"
		else:
			return "failed"
	elif question == "Look at this series: 53, 53, 40, 40, 27, 27, What number should come next?":
		if attempt == 14:
			return "passed"
		else:
			return "failed"
	elif question == "60 Times of 8 Equals to?":
		if attempt == 480:
			return "passed"
		else:
			return "failed"

	elif question == "What is the Next Prime Number after 7?":
		if attempt == 11:
			return "passed"
		else:
			return "failed"

	elif question == "The Product of 131 x 0 x 300 x 4":
		if attempt == 0:
			return "passed"
		else:
			return "failed"
	
	elif question == "Solve: 3 + 6 x (5 + 4) / 3 - 7":
		if attempt == 14:
			return "passed"
		else:
			return "failed"

	elif question == "Solve: 23 + 3 / 2":
		if attempt == 13:
			return "passed"
		else:
			return "failed"
	elif question == "What is 6% Equals to":
		if attempt == 0.06:
			return "passed"
		else:
			return "failed"

	elif question == "How Many Years are there in a Decade?":
		if attempt == 10:
			return "passed"
		else:
			return "failed"

	elif question == "How Many Months Make a Century?":
		if attempt == 1200:
			return "passed"
		else:
			return "failed"
	
	elif question == "How Many Sides are there in a Decagon?":
		if attempt == 10:
			return "passed"
		else:
			return "failed"

	elif question == "27 is a perfect cube. If true then what is the perfect cube of 27?":
		if attempt == 3:
			return "passed"
		else:
			return "failed"
	elif question == "Look at this series: 36, 34, 30, 28, 22 What number should come to fill in the blank space":
		if attempt == 24:
			return "passed"
		else:
			return "failed"

	elif question == "What is the sum of 130+125+191?":
		if attempt == 446:
			return "passed"
		else:
			return "failed"
	
	elif question == "110 divided by 10 is":
		if attempt == 11:
			return "passed"
		else:
			return "failed"
	elif question == "110 divided by 10 is":
		if attempt == 11:
			return "passed"
		else:
			return "failed"
	elif question == "Find the missing terms in multiple of 3: 3, 6, 9, __, 15":
		if attempt == 12:
			return "passed"
		else:
			return "failed"
	elif question == "Find the missing terms in multiple of 3: 3, 6, 9, __, 15":
		if attempt == 12:
			return "passed"
		else:
			return "failed"
	elif question == "What is the next prime number after 5?":
		if attempt == 7:
			return "passed"
		else:
			return "failed"
							
	elif question == "Solve: 300 – (150 x 2)":
		if attempt == 0:
			return "passed"
		else:
			return "failed"
					



total_number_of_question_passed = 0

questionattempt = 1
feedback = " "
for attempt in range(1, 11):

	question = arithmeticproblems()
	print(question)
	questionattempt = 0

	while questionattempt < 10:
		question_answer = int(input("Enter your answer:  "))
		feedback = grade(question_answer, question)
		print("question", feedback)


		if feedback == "passed":
			questionattempt = 10
			total_number_of_question_passed = total_number_of_question_passed + 1 
		else:
			questionattempt = questionattempt + 1

	print(" ")

if total_number_of_question_passed >= 10: 
	print(name + " Excellent, you passed with grade A : your score is 100")

elif total_number_of_question_passed < 10:
	print(name + " you passed with grade B : your score is 60")

elif total_number_of_question_passed <= 5: 
	print(name + " you passed with grade C : your score is 45")

elif total_number_of_question_passed == 0:
	print(miracle + " you failed with a grade of F....try again")


