# Write a program that asks for two numbers and prints the bigger one
a=input("A number: ")
b=input("Another number: ")
if int(a)>int(b):
    print(a)
elif int(a)<int(b):
    print(b)
else:print("They are even")