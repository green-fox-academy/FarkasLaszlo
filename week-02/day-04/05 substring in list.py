#Create a function that takes a string and a list of string as a parameter
#Returns the index of the string in the list where the first string is part of
#Returns -1 if the string is not part any of the strings in the list
#Example

#input: 'ching', ['this', 'is', 'what', 'I'm', 'searching', 'in']
#output: 4
input_string = ['this', 'is', 'what', 'I\'m', 'searching', 'in']
search_string = 'searching'

def search(string_list,string_to_find):
    if string_to_find in string_list:
        return string_list.index(string_to_find)
    return -1

print(search(input_string,search_string))