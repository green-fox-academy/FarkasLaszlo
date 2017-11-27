# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print �Fizz� instead of the number
# and for the multiples of five print �Buzz�.
# For numbers which are multiples of both three and five print �FizzBuzz�.
for n in range(1,101,1):
    if not n%3 and n%5:
        print('"Fizz"')
    elif not n%5 and n%3:
        print('"Buzz"')
    elif not n%3 and not n%5:
        print('"FizzBuzz"')
    else:print(n)