def character_swapper(first_character, second_character):
    combined_characters = ""
    first = first_character[0:2]
    second = second_character[0:2]
    new_first = second + first_character[2]
    new_second = first + second_character[2]

    combined_characters += new_first + " " + new_second

    return combined_characters


