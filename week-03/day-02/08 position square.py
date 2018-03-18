from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.
def square_draw(x,y):
    canvas.create_polygon(x, y, x + 50, y, x + 50, y + 50, x, y + 50)

square_draw(5, 5)
square_draw(100, 100)
square_draw(200, 200)

root.mainloop()