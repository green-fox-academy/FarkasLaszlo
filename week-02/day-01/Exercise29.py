# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
a = input('A number: ')
a = int(a)
n = 0
space = ' '
star = '*'
while n < a:
    print((a - n) * space + (2 * n + 1) * star)
    n += 1