from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]
for i in range(0, 150, 10):
    canvas.create_line(150, i, 150 + i, 150, fill='green')
    canvas.create_line(150 ,i, 150 - i, 150, fill='green')
    canvas.create_line(150, 300 - i, 150 + i, 150, fill='green')
    canvas.create_line(150, 300 - i, 150 - i, 150, fill='green')

root.mainloop()