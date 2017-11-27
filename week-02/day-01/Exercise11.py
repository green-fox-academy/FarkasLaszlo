a = 3
# make it bigger by 10
a += 10

print(a)

b = 100
# make it smaller by 7
b -= 7

print(b)

c = 44
# please double c's value
c *= 2


print(c)
d = 125
# please divide by 5 d's value 
d /= 5

print(d)

e = 8
# please cube of e's value
e = e**2

print(e)

f1 = 123
f2 = 345
# tell if f1 is bigger than f2 (pras a boolean)
if f1>f2:
    print(True)
else:print(False)

g1 = 350
g2 = 200
# tell if the double of g2 is bigger than g1 (pras a boolean)
if g1<g2*2:
    print(True)
else:print(False)


h = 1357988018575474
# tell if it has 11 as a divisor (pras a boolean)
if not h%11:
    print(True)
else:print(False)

i1 = 10
i2 = 3
# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)
if i1>i2**0.5 and i1<i2**2:
    print(True)
else:print(False)

j = 1521
# tell if j is dividable by 3 or 5 (pras a boolean)
if not j%5 or not j%3:
    print(True)
else:print(False)

k = "Apple"
#fill the k variable with its cotnent 4 times
k = k*4

print(k)
