input_string = 'dog goat dad duck doodle never'
input_string2 = 'racecar'
input_string3 = 'A Toyota! Race fast, safe car!'

def palindrome_search(input_str):
    result = list()
    result = palindromes(input_str, result)
    input_str = input_str.replace(' ', '').lower().replace(',', '').replace('!', '')
    result = palindromes(input_str, result)
    result = sorted(set(result))
    return result

def palindromes(string, search_result):
    length = 3
    while length <= len(string):
        for i in range(0, len(string) - 1, 1):
            x = string[i:i + length:1]
            if x == x[:: -1]:
                search_result.append(x)
        length += 1
    return search_result




print(palindrome_search(input_string))
print(palindrome_search(input_string2))
print(palindrome_search(input_string3))
