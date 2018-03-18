from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def draw_hex(border,x,y,r):
    canvas.create_polygon(x - r, y, x - border / 2, y + r, x + border / 2, y + r, x + r,
    y, x + border / 2, y - r, x - border / 2, y - r, fill='white', outline='black')

border = 20
r = ((3 ** 0.5) / 2) * border

def draw_single_hexa(range1, range2, x_value, y_value):
    y = y_value
    for j in range(range1):
        x = x_value
        for i in range(range2):
            draw_hex(border, x, y, r)
            x += 2 * r + border
        y += 2 * r

draw_single_hexa(7, 1, 150, 35)
draw_single_hexa(6, 2, 150 - border / 2 - r, 35 + r)
draw_single_hexa(5, 3, 150 - border - 2 * r, 35 + 2 * r)
draw_single_hexa(4, 4, 150 - 3 * (border / 2 + r), 35 + 3 * r)

root.mainloop()