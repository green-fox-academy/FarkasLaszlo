# - Create a two dimensional list
#   which can contain the different shades of specified colors
# - In `colors[0]` store the shades of green:
#   `"lime", "forest green", "olive", "pale green", "spring green"`
# - In `colors[1]` store the shades of red:
#   `"orange red", "red", "tomato"`
# - In `colors[2]` store the shades of pink:
#   `"orchid", "violet", "pink", "hot pink"`
a = [[0 for x in range(5)] for y in range(3)]
for x in range(3):
    for y in range(5):
        if x==0 and y==0:
            a[x][y]="lime"
        elif x==0 and y==1:
            a[x][y]="forest green"
        elif x==0 and y==2:
            a[x][y]="olive"
        elif x==0 and y==3:
            a[x][y]="pale green"
        elif x==0 and y==4:
            a[x][y]="spring green"
        elif x==1 and y==0:
            a[x][y]="orange red"
        elif x==1 and y==1:
            a[x][y]="red"
        elif x==1 and y==2:
            a[x][y]="tomato"
        elif x==2 and y==0:
            a[x][y]="orchid"
        elif x==2 and y==1:
            a[x][y]="violet"
        elif x==2 and y==2:
            a[x][y]="pink"
        elif x==2 and y==3:
            a[x][y]="hot pink"
    print(a[x])

print(a)