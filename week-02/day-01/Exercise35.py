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
while a<4:
    print(c+b+c+b+c+b+c+b)
    print(b+c+b+c+b+c+b+c)
    a+=1