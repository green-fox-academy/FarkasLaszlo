from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

a = 5
b = 15
diff = 10
for i in range(6):
    canvas.create_rectangle(a, a, b, b, fill='purple', outline='black')
    a += diff
    diff += 10
    b += diff

root.mainloop()