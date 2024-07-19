def vowels(word):
	vowelcount = 0
	count = 1
	while count <= 5: 
		if count == 1 and 'a' in word:
			vowelcount = vowelcount + 1
		elif count == 2 and 'e' in word:
			vowelcount = vowelcount + 1
		elif count == 3 and 'i' in word:
			vowelcount = vowelcount + 1
		elif count == 4 and 'o' in word:	
			vowelcount = vowelcount + 1
		elif count == 5 and 'u' in word:
			vowelcount = vowelcount + 1
		count = count + 1
	return vowelcount

def consonant(word):
	consonantcount = 0
	count = 1
	while count <= 21:
		if count == 1 and 'b' in word:
			consonantcount = consonantcount + 1
		elif count == 2 and 'c' in word:
			consonantcount = consonantcount + 1
		elif count == 3 and 'd' in word:
			consonantcount = consonantcount + 1
		elif count == 4 and 'f' in word:	
			consonantcount = consonantcount + 1
		elif count == 5 and 'g' in word:
			consonantcount = consonantcount + 1
		elif count == 6 and 'h' in word:
			consonantcount = consonantcount + 1
		elif count == 7 and 'j' in word:
			consonantcount = consonantcount + 1
		elif count == 8 and 'k' in word:	
			consonantcount = consonantcount + 1
		elif count == 9 and 'l' in word:
			consonantcount = consonantcount + 1
		elif count == 10 and 'm' in word:
			consonantcount = consonantcount + 1
		elif count == 11 and 'n' in word:	
			consonantcount = consonantcount + 1
		elif count == 12 and 'p' in word:
			consonantcount = consonantcount + 1
		elif count == 13 and 'q' in word:
			consonantcount = consonantcount + 1
		elif count == 14 and 'r' in word:	
			consonantcount = consonantcount + 1
		elif count == 15 and 's' in word:
			consonantcount = consonantcount + 1
		elif count == 16 and 't' in word:
			consonantcount = consonantcount + 1
		elif count == 17 and 'v' in word:	
			consonantcount = consonantcount + 1
		elif count == 18 and 'w' in word:
			consonantcount = consonantcount + 1
		elif count == 19 and 'x' in word:
			consonantcount = consonantcount + 1
		elif count == 20 and 'y' in word:	
			consonantcount = consonantcount + 1
		elif count == 21 and 'z' in word:
			consonantcount = consonantcount + 1
		count = count + 1
	
	return consonantcount





userinput = input("enter a word:  ")
vowels = vowels(userinput.lower())
consonant = consonant(userinput.lower())

print(f"we have {vowels} vowels in {userinput}, and {consonant} consonant")



