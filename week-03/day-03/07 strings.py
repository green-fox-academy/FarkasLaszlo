# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.
some_string = 'xzxyxzxyxabcyxy'
def strings(some_string):
    if some_string == '':
        return ''
    if some_string[0] == 'x':
        return 'y' + strings(some_string[1:])
    return some_string[0] + strings(some_string[1:])

new_string = strings(some_string)
print(new_string)
