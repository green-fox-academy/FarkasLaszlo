import turtle

def tree2(base, depth, angle):
    if base > depth:
        t.forward(base)
        t.right(angle)
        tree2(base - 3, depth, angle)
        t.left(2 * angle)
        tree2(base - 3, depth, angle)
        t.right(angle)
        t.backward(base)


t = turtle.Turtle()
hex = turtle.Screen()
t._tracer(0, 0)
t.color('yellow')
hex.bgcolor('black')
t.hideturtle()
t.speed(0)
t.penup()
t.left(90)
t.backward(250)
t.pendown()
tree2(50, 5, 13)
hex.update()
hex.exitonclick()