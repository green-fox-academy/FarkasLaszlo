import turtle

def lot_triangle(base,depth):
    if base > depth:
        t.speed(200)
        for i in range(3):
            t.forward(base)
            t.right(120)
        t.forward(base/2)
        t.right(60)
        t.forward(base/2)
        t.right(120)
        t.forward(base/2)
        t.right(120)
        t.forward(base/2)
        t.right(60)
        t.backward(base/2)
        lot_triangle(base/2,depth-1)
        t.forward(base/2)
        lot_triangle(base/2,depth-1)
        t.backward(base/2)
        t.right(60)
        t.forward(base/2)
        t.left(60)
        lot_triangle(base/2,depth-1)
        t.right(60)
        t.backward(base/2)
        t.left(60)





t = turtle.Turtle()
hex = turtle.Screen()
t.color("black")
t._tracer(0,0)
t.speed(0)
t.penup()
t.backward(300)
t.left(90)
t.forward(300)
t.right(90)
t.pendown()
lot_triangle(500,20)
hex.update()
hex.exitonclick()