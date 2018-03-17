# - Create a two dimensional list
#   which can contain the different shades of specified colors
# - In `colors[0]` store the shades of green:
#   `"lime", "forest green", "olive", "pale green", "spring green"`
# - In `colors[1]` store the shades of red:
#   `"orange red", "red", "tomato"`
# - In `colors[2]` store the shades of pink:
#   `"orchid", "violet", "pink", "hot pink"`
colors = [[0 for x in range(5)] for y in range(3)]
for x in range(3):
    for y in range(5):
        if x == 0 and y == 0:
            colors[x][y] = '"lime"'
        elif x == 0 and y == 1:
            colors[x][y] = '"forest green"'
        elif x == 0 and y == 2:
            colors[x][y] = '"olive"'
        elif x == 0 and y == 3:
            colors[x][y] = '"pale green"'
        elif x == 0 and y == 4:
            colors[x][y] = '"spring green"'
        elif x == 1 and y == 0:
            colors[x][y] = '"orange red"'
        elif x == 1 and y == 1:
            colors[x][y] = '"red"'
        elif x == 1 and y == 2:
            colors[x][y] = '"tomato"'
        elif x == 2 and y == 0:
            colors[x][y] = '"orchid"'
        elif x == 2 and y == 1:
            colors[x][y] = '"violet"'
        elif x == 2 and y == 2:
            colors[x][y] = '"pink"'
        elif x == 2 and y == 3:
            colors[x][y] = '"hot pink"'
        if colors[x][y] != 0:
            print(colors[x][y], end=' ')
    print('')
