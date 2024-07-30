created_list = []
for num in range(1, 10):
	created_list = created_list +  [num]

print(created_list)

letters = []
letters += ('grace', 'shola')
print(letters)

first_list = [20, 50, 'grace']
second_list = [34, 55, 'hope']

third_list = first_list + second_list
print(third_list)

for count in range(len(third_list)):
	print(count,:', third_list[count])