from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
canvas.create_polygon(5, 5, 5, 20, 20, 20, 20, 5, fill='green')
canvas.create_polygon(50, 50, 50, 100, 100, 100, 100, 50, fill='blue')
canvas.create_polygon(150, 150, 250, 150, 250, 200, 150, 200, fill='red')
canvas.create_polygon(100, 150, 150, 150, 150, 250, 100, 250, fill='orange')

root.mainloop()