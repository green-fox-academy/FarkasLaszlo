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
a = input("A number: ")
a = int(a)
n = 0
c = " "
b = "*"
while n<=a/2:
    print((a-n)*c,(2*n+1)*b,(a-n)*c)
    n +=1
n-=2
while 0<=n<a/2:
    print((a-n)*c,(2*n+1)*b,(a-n)*c)
    n -=1
