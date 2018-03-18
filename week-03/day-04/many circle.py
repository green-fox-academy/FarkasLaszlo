import turtle

def yellow_box(base, depth):
    if base > depth:
        t.speed(200)
        for i in range(3):
            t.circle(base, 120)
            t.circle(base / 2)
        for i in range(3):
            t.circle(base, 120)
            yellow_box(base / 2, depth)




t = turtle.Turtle()
hex = turtle.Screen()
t._tracer(0, 0)
t.penup()
t.left(90)
t.backward(300)
t.right(90)
t.circle(300, 180)
t.pendown()
t.color('black')
yellow_box(300, 10)
hex.update()
hex.exitonclick()