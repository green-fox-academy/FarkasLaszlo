# Adds a and b, returns as result
def add(a, b):
    summa = a + b
    return summa


# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Returns the median value of a list given as param
def median(pool):
    summa = 0
    for i in range(len(pool)):
        summa += pool[i]
    return summa/len(pool)


# Returns true if the param is a vovel
def is_vovel(char):
    if len(char) == 1:
        if char in 'aeiouéáőűöüóí':
            return char
        elif char in 'AEIOUÉÁŐŰÖÜÓÍ':
            return char


# Create a method that translates hungarian into the teve language
def translate(hungarian):
    if hungarian == "":
        return ""
    elif hungarian[0] in "aeiouéáőűöüóí" or hungarian[0] in "AEIOUÉÁŐŰÖÜÓÍ":
        if hungarian[0] in "AEIOUÉÁŐŰÖÜÓÍ":
            return hungarian[0] + "v" + hungarian[0].lower() + translate(hungarian[1:])
        return hungarian[0] + "v" + hungarian[0] + translate(hungarian[1:])
    else:
        return hungarian[0] + translate(hungarian[1:])
