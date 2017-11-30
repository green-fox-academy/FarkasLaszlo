def josephus(n):
    p = 1
    while p<= n:
        p *= 2
    return (2*n) - p+1

print(josephus(1))
print(josephus(2))
print(josephus(3))
print(josephus(7))
print(josephus(12))
print(josephus(41))