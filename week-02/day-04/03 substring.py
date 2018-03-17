input_string = 'this is what I\'m searching in'
search_string = 'searching'

def search(input_string,search_string):
    for i in range(len(input_string)):
        if input_string[i:i + len(search_string)] == search_string:
            return i
    return -1

print(search(input_string,search_string))
