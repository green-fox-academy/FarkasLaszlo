# - Write a function called `sum` that sum all the numbers
#   until the given parameter
a=0
def sum(a):
    b = 0
    n = 0
    a = input("A number: ")
    a = int(a)
    i = a
    while not n==i:
        b = b + a
        a -= 1
        n += 1

    return b

print(sum(a))


