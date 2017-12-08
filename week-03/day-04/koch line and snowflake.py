import turtle


def koch(base,depth):
    if depth==0:
        t.forward(base)
    elif base > depth:
        t.speed(0)
        koch(base/3,depth-1)
        t.left(60)
        koch(base/3,depth-1)
        t.right(120)
        koch(base/3,depth-1)
        t.left(60)
        koch(base/3,depth-1)



def snowflake():
    for i in range(3):
        koch(300,5)
        t.right(120)



t = turtle.Turtle()
hex = turtle.Screen()
t._tracer(0,0)
t.color("black")
t.speed(0)
t.penup()
t.backward(250)
t.left(90)
t.forward(150)
t.right(90)
t.pendown()
snowflake()
hex.update()
hex.exitonclick()