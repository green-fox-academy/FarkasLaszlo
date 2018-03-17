# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output
n = 4
a = [[0 for x in range(n)] for y in range(n)]
for x in range(n):
    for y in range(n):
        if x == y:
            a[x][y] = 1
        else: 
            a[x][y] = 0
        print(a[x][y], end=' ')
    print()
