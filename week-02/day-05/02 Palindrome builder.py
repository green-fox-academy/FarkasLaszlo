string = "greenfox"

def palindrome(string):
    new_string = string
    new_string += string[::-1]
    return new_string

print(palindrome(string))