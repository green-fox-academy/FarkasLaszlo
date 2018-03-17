string = 'greenfox'

def palindrome(string):
    string += string[::-1]
    return string

print(palindrome(string))