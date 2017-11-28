# - Write a function called `sum` that sum all the numbers
#   until the given parameter
a=0
def sum(a):
    b = 0
    a = input("A number: ")
    a = int(a)
    b = a*(a+1)/2
    return b

print(sum(a))
