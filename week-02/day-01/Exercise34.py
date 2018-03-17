# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4
a = 0
b = 0
c = 0
n = input('The number: ')
n = int(n)
if a == 0 and n > 0:
    b = input('Type the first number: ')
    b = int(b)
    c = b
    a += 1
while a < n:
    b = input('Type another number: ')
    b = int(b)
    c = c + b
    a += 1
print('Sum: ', c, 'Average: ', c / n)