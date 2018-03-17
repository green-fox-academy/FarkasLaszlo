# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was
a = input('A number: ')
a = int(a)
a -= 1
n = 1
sign = '%'
space = ' '
print((a + 1) * sign)
while n < a:
    print(sign + (n - 1) * space + sign + (a - n - 1) * space + sign)
    n += 1
print((a + 1) * sign)