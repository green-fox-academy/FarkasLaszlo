from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.

canvas.create_line(0, 0, 300, 300, fill="#00FF00")
canvas.create_line(300, 0, 0, 300, fill="#00FF00")

root.mainloop()