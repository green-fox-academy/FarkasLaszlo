# L(n,2)= 1 + 2n - 2^(1 + (lg n))
# n = 1 ==> L = 1
# n = 2 ==> L = 1
# n = 3 ==> L = 3
# n = 4 ==> L = 1
# n = 8 ==> L = 1
def josephus_a(n):
    p = 1
    c = 0
    while p <= n:
        p *= 2
        c = 1 + (2 * n) - p
    return c

print(josephus_a(1))
print(josephus_a(2))
print(josephus_a(3))
print(josephus_a(7))
print(josephus_a(12))
print(josephus_a(41))


import math
def josephus_b(n):
    a = 0
    a = 1 + 2 * n - 2 ** (1 + int(math.log(n, 2)))
    return a

print(josephus_b(1))
print(josephus_b(2))
print(josephus_b(3))
print(josephus_b(7))
print(josephus_b(12))
print(josephus_b(41))
