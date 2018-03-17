# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have
a = input('Chicken: ')
b = input('Pigs: ')
legs = int(a) * 2 + int(b) * 4
print('The number of legs: ' + str(legs) )