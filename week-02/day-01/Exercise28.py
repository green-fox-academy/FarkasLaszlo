# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was
a = input("A number: ")
a = int(a)
b = "*"
n = 0
while n<a:
    n+=1
    print(n*b)