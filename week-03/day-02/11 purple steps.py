from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]
# 19 little purple box
for i in range(19):
    canvas.create_rectangle(5+10*i,5+10*i,15+10*i,15+10*i,fill="purple",outline="black")

root.mainloop()