input_string = "dog goat dad duck doodle never"

def palindrome_search(input_string):
    a = list()
    length = 3
    while length <= len(input_string):
        for i in range(0, len(input_string)-1, 1):
            x = input_string[i:i+length:1]
            if x == x[::-1]:
                a.append(x)
        length += 1

    print(a)

palindrome_search(input_string)
