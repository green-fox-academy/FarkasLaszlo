from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
def line_draw(x,y):
    canvas.create_line(x, y, 150, 150)

line_draw(10, 10)
line_draw(100, 200)
line_draw(200, 150)

root.mainloop()