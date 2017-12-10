import turtle

def lot_hex(base,depth):
    if base > depth:
        t.speed(200)
        for i in range(6):
            t.forward(base)
            t.right(60)
        for x in range(3):
            lot_hex(base/2,depth-1)
            for i in range(6):
                t.forward(base/2)
                t.right(60)
            for i in range(2):
                t.forward(base)
                t.right(60)


t = turtle.Turtle()
hex = turtle.Screen()
t._tracer(0,0)
t.hideturtle()
t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.pendown()
t.color("black")
lot_hex(200,10)
hex.update()
hex.exitonclick()





