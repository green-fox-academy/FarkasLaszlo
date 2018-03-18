from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.

canvas.create_line(100, 100, 100, 200, fill='#FF0000')
canvas.create_line(100, 100, 200, 100, fill='#00FF00')
canvas.create_line(200, 100, 200, 200, fill='#0000FF')
canvas.create_line(100, 200, 200, 200, fill='#FF00FF')

root.mainloop()