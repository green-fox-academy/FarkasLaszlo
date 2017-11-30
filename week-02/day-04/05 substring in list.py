#Create a function that takes a string and a list of string as a parameter
#Returns the index of the string in the list where the first string is part of
#Returns -1 if the string is not part any of the strings in the list
#Example

#input: "ching", ["this", "is", "what", "I'm", "searching", "in"]
#output: 4
input_string = ["this", "is", "what", "I'm", "searching", "in"]
search_string = "searching"

def search(input_string,search_string):
    for i in range(len(input_string)):
        for x in range(len(input_string[i])):
            if input_string[i][0:x+1] == search_string:
                return i
    return -1

print(search(input_string,search_string))