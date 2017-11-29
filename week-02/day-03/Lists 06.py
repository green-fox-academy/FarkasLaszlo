# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def contain(list_of_numbers):
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(len(list_of_numbers)):
        if a == 0 and list_of_numbers[i] == 4:
            a = 1
        elif b == 0 and list_of_numbers[i] == 8:
            b = 1
        elif c == 0 and list_of_numbers[i] == 12:
            c = 1
        elif d == 0 and list_of_numbers[i] == 16:
            d = 1

    if a + b + c + d == 4:
        return True
    else: return False

print(contain(list_of_numbers))