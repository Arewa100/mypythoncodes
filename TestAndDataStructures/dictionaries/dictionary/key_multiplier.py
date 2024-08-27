def key_multiplier(list_values):
    dictionary_pairs = {}
    for value in range(len(list_values)):
        dictionary_pairs[list_values[value]] = list_values[value] * list_values[value] * list_values[value]
    return dictionary_pairs
