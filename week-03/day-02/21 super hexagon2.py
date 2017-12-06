from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_hex(border,x,y,r):
    canvas.create_polygon(x-r,y,x-border/2,y+r,x+border/2,y+r,x+r,y,x+border/2,y-r,x-border/2,y-r,fill="white",outline="black")


y = 35
border = 20
r = ((3 ** 0.5) / 2) * border
for j in range(7):
    x = 150
    for i in range(1):
        draw_hex(border,x,y,r)
        x += 2*r+border
    y += 2*r

y = 35 + r
for j in range(6):
    x = 150 - border/2 -r
    for i in range(2):
        draw_hex(border,x,y,r)
        x += 2*r+border
    y += 2*r

y = 35 + 2*r
for j in range(5):
    x = 150 - border -2*r
    for i in range(3):
        draw_hex(border,x,y,r)
        x += 2*r+border
    y += 2*r


y = 35 + 3*r
for j in range(4):
    x = 150 - 3*(border/2 +r )
    for i in range(4):
        draw_hex(border,x,y,r)
        x += 2*r+border
    y += 2*r

root.mainloop()