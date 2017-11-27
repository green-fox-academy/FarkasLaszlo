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
a = input("A number: ")
a = int(a)
n = 0
c = " "
b = "*"
while n<a:
    print((a-n)*c,(2*n+1)*b,(a-n)*c)
    n +=1