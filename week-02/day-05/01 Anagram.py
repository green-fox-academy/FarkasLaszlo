input_string1 = 'safetyrail'
input_string2 = 'Fairytales'


def anagram(input_1, input_2):
    input_1 = input_1.replace(' ', '')
    input_2 = input_2.replace(' ', '')
    input_1 = sorted(input_1.lower())
    input_2 = sorted(input_2.lower())
    if input_1 == input_2:
        return True
    else:
        return False


print(anagram(input_string1, input_string2))
