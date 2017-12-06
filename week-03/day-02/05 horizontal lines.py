from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.
def horizontal_draw(x,y):
    canvas.create_line(x,y,x+50,y)


horizontal_draw(0,10)
horizontal_draw(15,25)
horizontal_draw(50,50)

root.mainloop()