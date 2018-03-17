# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#
space = " "
sign = "%"
n = 4
for i in range(n):
    print((sign + space) * n)
    print((space + sign) * n)