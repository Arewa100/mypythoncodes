def word_splitter(word_input):
    if type(word_input) == str:
        character_count_pairs = split_and_count(word_input)
    else:
        raise TypeError("not a word")
    return character_count_pairs

def split_and_count(word_input):
    word = word_input.lower()
    character_count_pairs = {}
    WORD_LENGTH = len(word)
    for count in range(WORD_LENGTH):
        character_count = 0
        character = word[count]
        for letter in word:
            if character == letter:
                character_count += 1
        character_count_pairs[character] = character_count
    return character_count_pairs

print(word_splitter("showww"))