from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a green 10x10 square to the center of the canvas.
canvas.create_polygon(145, 145, 155, 145, 155, 155, 145, 155, fill='white', outline='green')

root.mainloop()