import turtle
import random


def rgbhex(r,g,b):
    return '#%02x%02x%02x' % (r, g, b)


def square_grid(base, depth, pensize):
    if base > depth:
        t.speed(200)
        t.pensize(pensize)
        t.penup()
        t.forward(base/4)
        t.right(90)
        t.forward(base/4)
        t.left(90)
        t.pendown()
        t.color("black",rgbhex(random.randint(50, 220), random.randint(50, 220), random.randint(50, 220)))
        t.begin_fill()
        for i in range(4):
            t.forward(base/2)
            t.right(90)
        t.end_fill()
        t.left(90)
        t.penup()
        t.forward(base/4)
        t.right(90)
        t.backward(base/4)
        t.pendown()
        t.color("black","black")
        for i in range(4):
            t.penup()
            t.forward(base/2)
            t.pendown()
            square_grid(base/2, depth, pensize/2)
            t.penup()
            t.forward(base/2)
            t.pendown()
            t.right(90)


t = turtle.Turtle()
hex = turtle.Screen()
t._tracer(0,0)
t.penup()
t.left(90)
t.forward(300)
t.right(90)
t.backward(300)
t.pendown()
t.pensize(10)
t.color("black", "black")
square_grid(random.randint(400, 600), 20, 12)
hex.update()
hex.exitonclick()
