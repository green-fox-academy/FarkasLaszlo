from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.
def draw_centerline(x, y):
    canvas.create_line(x, y, 150, 150)

for i in range(31):
    draw_centerline(i * 10, 0)
    draw_centerline(0, i * 10)
    draw_centerline(i * 10, 300)
    draw_centerline(300, i * 10)

root.mainloop()