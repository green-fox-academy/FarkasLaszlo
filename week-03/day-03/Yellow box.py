import turtle

def yellow_box(base,depth):
    if base > depth:
        t.speed(200)
        for i in range(4):
            t.forward(base)
            t.right(90)
        for x in range(4):
            t.forward(base/3)
            yellow_box(base/3,depth)
            for i in range(4):
                t.forward(base/3)
                t.right(90)
            t.forward(2*base/3)
            t.right(90)




t = turtle.Turtle()
hex = turtle.Screen()
t._tracer(0,0)
hex.bgcolor("yellow")
t.penup()
t.left(90)
t.forward(300)
t.right(90)
t.backward(300)
t.pendown()
t.color("black")
yellow_box(600,5)
hex.update()
hex.exitonclick()