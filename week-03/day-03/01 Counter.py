# Write a recursive function that takes one parameter: n and counts down from n.
def count(n):
    print(n)
    if n <= 1:
        return 1
    else:
        return count(n-1)

count(9)