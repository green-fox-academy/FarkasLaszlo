# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8
a = 0
n = 0
while(n == 0):
    a = input('The number: ')
    a = int(a)
    if a == 8:
        print('You found the number: ' + str(a))
        n += 1
    elif a < 8:
        print('The stored number is higher')
    elif a > 8:
        print('The stored number is lower')

