# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was
a = input('A number: ')
a = int(a)
a -= 1
n = 0
space = ' '
star = '*'

for i in range(1, a + 2):
    if(i <= a / 2):
        print((a - n) * space,(2 * n + 1) * star)
        n += 1
    if(i > a / 2):
        print((a - n) * space,(2 * n + 1) * star)
        n -= 1