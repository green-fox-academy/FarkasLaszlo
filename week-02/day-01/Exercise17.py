# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
print("Type in five number!")
a=input("1.: ")
b=input("2.: ")
c=input("3.: ")
d=input("4.: ")
e=input("5.: ")
sum= int(a)+int(b)+int(c)+int(d)+int(e)
average=sum/5
print("Sum: ",sum,"Average: ", average )