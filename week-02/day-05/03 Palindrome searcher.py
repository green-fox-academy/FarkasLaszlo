input_string = "dog goat dad duck doodle never"
input_string2 = "racecar"
input_string3 = "A Toyota! Race fast, safe car!"

def palindrome_search(input_str):
    a = list()
    length = 3
    while length <= len(input_str):
        for i in range(0, len(input_str)-1, 1):
            x = input_str[i:i+length:1]
            if x == x[::-1]:
                a.append(x)
        length += 1

    input_str = input_str.replace(" ", "").lower().replace(",","").replace("!","")
    length = 3
    while length <= len(input_str):
        for i in range(0, len(input_str)-1, 1):
            x = input_str[i:i+length:1]
            if x == x[::-1]:
                a.append(x)
        length += 1
    a = sorted(set(a))
    return a



print(palindrome_search(input_string))
print(palindrome_search(input_string2))
print(palindrome_search(input_string3))
