# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def contain(numbers):
    valid = 0
    check_list = [4, 8, 12, 16]
    for i in check_list:
        if i in numbers:
            valid += 1

    if valid == len(check_list):
        return True
    return False

print(contain(list_of_numbers))