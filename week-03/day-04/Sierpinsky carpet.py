import turtle

def carpet(base, depth):
    if base > depth:
        t.speed(0)
        t.penup()
        t.forward(base / 3)
        t.right(90)
        t.forward(base / 3)
        t.left(90)
        t.begin_fill()
        for i in range(4):
            t.forward(base / 3)
            t.right(90)
        t.end_fill()
        t.left(90)
        t.forward(base / 3)
        t.right(90)
        t.backward(base / 3)
        carpet(base / 3, depth - 1)
        for x in range(4):
            for i in range(2):
                t.forward(base / 3)
                carpet(base / 3,depth - 1)
            t.forward(base / 3)
            t.right(90)


t = turtle.Turtle()
hex = turtle.Screen()
t._tracer(0, 0)
t.color('black', 'black')
t.speed(0)
t.penup()
t.backward(200)
t.left(90)
t.forward(300)
t.right(90)
t.pendown()
carpet(500, 10)
hex.update()
hex.exitonclick()