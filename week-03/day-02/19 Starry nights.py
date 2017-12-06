from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300',bg="black")
canvas.pack()
def rgbhex(r,g,b):
   return '#%02x%02x%02x' % (r, g, b)
# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)
for i in range(50):
    x = random.randint(10,290)
    y = random.randint(10,290)
    randomnumber = random.randint(1,5)
    randomcolor = random.randint(120,220)
    canvas.create_oval(x,y,x + randomnumber,y + randomnumber,fill=rgbhex(randomcolor,randomcolor,randomcolor))


root.mainloop()