def sequence(* variable_length_arguments):
    the_list= []
    the_new_list=[]
    the_list+= variable_length_arguments
    for number in the_list:
        the_converted_number = str(number)
        the_new_list.append(the_converted_number)
    the_tuple = tuple(the_new_list)
    the_result_as_a_string = f"{the_new_list}, {the_tuple}"
    return the_result_as_a_string