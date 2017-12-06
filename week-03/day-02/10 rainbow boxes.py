from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
def rgbhex(r,g,b):
   return '#%02x%02x%02x' % (r, g, b)

def rainbow_box(x,color):
        if x < 25:
            canvas.create_rectangle(150-x/2,150-x/2,150+x/2,150+x/2,fill=rgbhex(color,0,0))
        elif 25 <= x < 50:
            canvas.create_rectangle(150-x/2,150-x/2,150+x/2,150+x/2,fill=rgbhex(color,color,0))
        elif 50 <= x < 75:
            canvas.create_rectangle(150-x/2,150-x/2,150+x/2,150+x/2,fill=rgbhex(color,0,color))
        elif 75 <= x < 100:
            canvas.create_rectangle(150-x/2,150-x/2,150+x/2,150+x/2,fill=rgbhex(0,color,color))
        elif 100 <= x < 125:
            canvas.create_rectangle(150-x/2,150-x/2,150+x/2,150+x/2,fill=rgbhex(0,0,color))
        elif x > 125:
            canvas.create_rectangle(150-x/2,150-x/2,150+x/2,150+x/2,fill=rgbhex(0,color,0))

for i in range(200,0,-10):
    if i > 150:
        color = random.randint(50,220)
        rainbow_box(i,color)
    elif 100 < i <= 150:
        color = random.randint(50,220)
        rainbow_box(i,color)
    elif 16< i < 100:
        color = random.randint(50,220)
        rainbow_box(i,color)


root.mainloop()