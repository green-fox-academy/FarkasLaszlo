# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000
a = input("First side of the cube: ")
b = input("Second side of the cube: ")
c = input("Third side of the cube: ")
a = int(a)
b = int(b)
c = int(c)
surface = a*b*2 + b*c*2 + c*a*2
volume = a*b*c
print("Surface Area:",surface)
print("Volume:",volume)