from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a red horizontal line to the canvas' middle.
# draw a green vertical line to the canvas' middle.
y = int(300 / 2)
canvas.create_line(0, y, 300, y, fill='#FF0000')
x = int(300 / 2)
canvas.create_line(x, 0, x, 300, fill='#00FF00')

root.mainloop()