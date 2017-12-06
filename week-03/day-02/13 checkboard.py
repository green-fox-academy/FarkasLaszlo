from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.
for n in range(0,10,2):
    for i in range(0,10,2):
        canvas.create_rectangle(i*30,n*30,30*(i+1),(n+1)*30,fill="black")
        canvas.create_rectangle(30*(i+1),n*30,30*(i+2),(n+1)*30,fill="white")
for n in range(1,11,2):
    for i in range(0,10,2):
        canvas.create_rectangle(i*30,n*30,30*(i+1),(n+1)*30,fill="white")
        canvas.create_rectangle(30*(i+1),n*30,30*(i+2),(n+1)*30,fill="black")



root.mainloop()