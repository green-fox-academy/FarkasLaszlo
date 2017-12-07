# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def square(base, n):
    if base == 0:
        return 0
    elif n == 1:
        return base
    else:
        return base*square(base,n-1)

print(square(4,2))