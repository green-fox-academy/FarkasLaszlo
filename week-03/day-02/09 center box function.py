from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.
def draw_centerbox(x):
    canvas.create_polygon(150 - x / 2, 150 - x / 2, 150 - x / 2, 150 + x / 2, 150 + x / 2,
    150 + x / 2, 150 + x / 2, 150 - x / 2, fill='white', outline='black')


draw_centerbox(125)
draw_centerbox(100)
draw_centerbox(75)
draw_centerbox(50)
draw_centerbox(25)
draw_centerbox(1)
root.mainloop()