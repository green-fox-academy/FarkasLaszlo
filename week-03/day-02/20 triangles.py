from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

m = ((300**2-150**2)**0.5)/21
print(m)
a = 300/21
print(a)

for x in range(21):
    for i in range(x):
        canvas.create_polygon(1+a/2*(20-x)+a*i,300-m*(20-x),1+a/2*(20-x)+a*(i+1),300-m*(20-x),1+a/2*(21-x)+a*i,300-m*(21-x), fill="white",outline="black")

root.mainloop()