import random

b = input("The range: ")
b = int(b)
number = random.randint(1,b)
n = 0
while(n==0):
    a = input("Your guess: ")
    a= int(a)
    if a==number:
        print("You found the number: ", a)
        n +=1
    elif a<number:
        print("The stored number is higher")
    elif a>number:
        print("The stored number is lower")

print("You found the number: ", a)



