def character_swapper(first_string, second_string):
    combined_strings = ""
    first_string_sliced = first_string[0:2]
    second_string_sliced = second_string[0:2]
    first_new_string = first_string_sliced + second_string[2]
    second_new_string = second_string_sliced + first_string[2]

    combined_strings += second_new_string + " " + first_new_string

    return combined_strings

def character_placer(first_string, second_string):
    the_second_string = second_string + ""
    combined_strings = ""
    SECOND_STRING_LENGTH = len(the_second_string)
    FIRST_STRING_LENGTH = len(first_string)
    NEW_LENGTH = SECOND_STRING_LENGTH + FIRST_STRING_LENGTH
    if SECOND_STRING_LENGTH % 2 == 0:
        new_index = SECOND_STRING_LENGTH // 2
        for count in range(SECOND_STRING_LENGTH):
            if count == new_index:
                combined_strings += first_string[0]
            elif count == new_index + 1:
                combined_strings += first_string[1]
            else:
                combined_strings += the_second_string[count]

    return combined_strings

def word_sorter(word):
    lower_letters = ""
    upper_case__letters = ""
    for letter in word:
        if letter.isupper():
            upper_case__letters += letter
        else:
            lower_letters += letter
    arranged_word = upper_case__letters + lower_letters
    return arranged_word

def character_occurrence_checker(first_string, character):
    number_of_occurrences = first_string.count(character)
    return character, number_of_occurrences
