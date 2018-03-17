# - Create a function called `factorio`
#   that returns it's input's factorial
def factorio():
    a = input('A number: ')
    a = int(a)
    b = a
    while a > 1:
        a -= 1
        b *= a
    return b

print(factorio())
