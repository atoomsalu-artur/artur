import turtle

t  = turtle.Turtle()
t.speed(3)
t.pensize(2)
t.color("black")

def  draw_square(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)

draw_square(-100, 50, 150)
draw_square(-30, -180, -150)

turtle.done
