# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a '*'.
some_string = 'abcdefghijklmno'
def strings(some_string):
    if some_string == '':
        return ''
    if not some_string[0] == '':
        return '*' + some_string[0] +  strings(some_string[1:])

new_string = strings(some_string)
print(new_string)