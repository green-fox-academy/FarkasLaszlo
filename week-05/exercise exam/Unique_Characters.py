# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]


def unique_character(input_string):
    input_string = input_string.replace(" ", "")
    unique_list = []
    repeat_list = []
    final_list = []
    for i in range(len(input_string)):
        if input_string[i] not in unique_list:
            unique_list.append(input_string[i])
        elif input_string[i] in unique_list and input_string[i] not in repeat_list:
            repeat_list.append(input_string[i])
    for i in range(len(unique_list)):
        if unique_list[i] not in repeat_list:
            final_list.append(unique_list[i])
    return final_list

