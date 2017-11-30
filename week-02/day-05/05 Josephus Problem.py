# L(n,2)= 1 + 2n - 2^(1 + (lg n))
# n = 1 ==> L = 1
# n = 2 ==> L = 1
# n = 3 ==> L = x
# n = 4 ==> L = 1
# n = 8 ==> L = 1

def josephus(n):
    p = 1
    c = 0
    while p <= n:
        p *= 2
        c = 1 + (2 * n) - p
    return c

print(josephus(1))
print(josephus(2))
print(josephus(3))
print(josephus(7))
print(josephus(12))
print(josephus(41))
