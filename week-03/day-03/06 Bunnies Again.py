# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

def weird_bunnies(n):
    if n % 2 and n > 0:
        return weird_bunnies(n - 1) + 2
    elif not n % 2 and n > 0:
        return weird_bunnies(n - 1) + 3
    elif n <= 0:
        return 0

print(weird_bunnies(0))
print(weird_bunnies(1))
print(weird_bunnies(2))
print(weird_bunnies(3))
print(weird_bunnies(4))
print(weird_bunnies(5))