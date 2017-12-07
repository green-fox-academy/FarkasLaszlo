# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def bunny(n):
    if n > 0:
        return bunny(n-1) + 2
    if n <=0:
        return 0

print(bunny(8))