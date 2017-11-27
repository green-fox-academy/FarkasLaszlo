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
b= " "
c= "%"
a=0
n=4
while a<n:
    print((c+b)*n)
    print((b+c)*n)
    a+=1