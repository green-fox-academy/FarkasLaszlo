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
a = input("A number: ")
a = int(a)
n = 2
b = "%"
c = " "
print(a*b)
while n<a:
    print(b,(a-4)*c,b)
    n+=1
print(a*b)