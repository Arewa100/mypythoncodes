print("welcome friend")

number = int(input("'Enter a number: "))

first_index = (number // 10)
number = number % 10

second_index = (first_index // 10)
first_index = (first_index % 10)

third_index = (second_index // 10)
second_index = (second_index % 10)

fourth_index = (third_index // 10)
third_index = (third_index % 10)

print(fourth_index, third_index, second_index, first_index, number)