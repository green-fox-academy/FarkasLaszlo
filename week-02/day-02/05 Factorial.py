# - Create a function called `factorio`
#   that returns it's input's factorial
a = 0
def factorio(a):
    a = input("A number: ")
    a = int(a)
    b = a
    while a>1:
        a -= 1
        b *= a
    return b

print(factorio(a))
