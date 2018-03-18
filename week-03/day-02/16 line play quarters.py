from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]
for i in range(20, 300, 20):
    canvas.create_line(150 + i / 2, 0, 300, i / 2, fill='purple')
for i in range(20, 300, 20):
    canvas.create_line(i / 2, 300, 0, 150 + i / 2, fill='green')
for i in range(20, 300, 20):
    canvas.create_line(0, 150 - i / 2, i / 2, 0, fill='red')
for i in range(20, 300, 20):
    canvas.create_line(150 + i / 2, 300, 300, 300 - i / 2, fill='blue')

root.mainloop()