from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

def draw(color):
    for i in range(20,300,20):
        if color == 'purple':
            canvas.create_line(i, 0, 300, i, fill=color)
        elif color == 'green':
            canvas.create_line(i, 300, 0, i, fill=color)

draw('purple')
draw('green')

root.mainloop()