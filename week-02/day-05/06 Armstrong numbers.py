
number = input('Your number: ')
number = int(number)
a = [int(i) for i in str(number)]
n = len(a)
b = 0
for i in range(len(a)):
    b = b + a[i] ** n
if b == number:
    print('The', number, 'is an Armstrong number')
else:
    print('The', number, 'is not an Armstrong number')
