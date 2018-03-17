# - Write a function called `sum` that sum all the numbers
#   until the given parameter
def sum():
    a = input('A number: ')
    a = int(a)
    a = a * (a + 1) / 2
    return a

print(sum())
