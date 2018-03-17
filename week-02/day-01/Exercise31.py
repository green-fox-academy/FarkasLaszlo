# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was
a = input('A number: ')
a = int(a)
n = 2
sign = '%'
space = ' '
print(a * sign)
while n < a:
    print(sign + (a - 2) * space + sign)
    n += 1
print(a * sign)