# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ['Eve', 'Ashley', 'Bözsi', 'Kat', 'Jane']
boys = ['Joe', 'Fred', 'Béla', 'Todd', 'Neef', 'Jeff']
order = []
length = 0
if len(girls) > len(boys):
    length = len(girls)
else:
    length = len(boys)
i = 0
for n in range(length * 2):
    order[i:i + 1] = girls[n:n + 1]
    i += 1
    order[i:i + 1] = boys[n:n + 1]
    i += 1

print(order)
