def get_length(word):
	total_length = 0
	feed = list(word)
	for character in feed:
		total_length = total_length + 1
	return total_length

result = get_length([1, 2, 3, 4])
print(result)
