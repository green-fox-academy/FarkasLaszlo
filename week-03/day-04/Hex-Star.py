import turtle


def star(base,depth):
    if base > depth:
        t.speed(0)
        t.begin_fill()
        for i in range(6):
            t.forward(base)
            t.right(60)
        t.end_fill()
        star(base/3,depth-1)
        for i in range(6):
            t.forward(base/3)
            t.right(60)
        t.forward(2*base/3)
        star(base/3,depth-1)
        for i in range(7):
            t.forward(base/3)
            t.right(60)
        t.forward(2*base/3)
        star(base/3,depth-1)
        for i in range(7):
            t.forward(base/3)
            t.right(60)
        t.forward(2*base/3)
        star(base/3,depth-1)
        for i in range(7):
            t.forward(base/3)
            t.right(60)
        t.forward(2*base/3)
        star(base/3,depth-1)
        for i in range(7):
            t.forward(base/3)
            t.right(60)
        t.forward(2*base/3)
        star(base/3,depth-1)
        for i in range(7):
            t.forward(base/3)
            t.right(60)
        t.forward(base)
        t.right(60)



t = turtle.Turtle()
hex = turtle.Screen()
hex.bgcolor("grey")
t._tracer(0,0)
t.color("black")
t.fillcolor("white")
t.speed(0)
t.penup()
t.backward(200)
t.left(90)
t.forward(300)
t.right(90)
t.pendown()
star(300,10)
hex.update()
hex.exitonclick()

