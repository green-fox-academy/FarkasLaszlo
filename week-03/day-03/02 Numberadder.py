# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.
def count(n):
    if n <= 1:
        return 1
    else:
        return count(n - 1) + n


print(count(9))