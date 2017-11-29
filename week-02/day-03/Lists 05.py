 #Check if the list contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

numbers = [1, 2, 3, 4, 5, 6, 8]

for i in range(len (numbers)):
    a = 0
    if numbers[i] == 7:
        a+=1

if a == 1:
    print("Hoorray")
else:
    print("Noooooo")