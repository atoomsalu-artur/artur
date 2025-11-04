import turtle

t = turtle.Turtle()

for _ in range(4):
    t.forward(100)
    t.right(90)

t.penup()

t.penup()
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.pendown()

for _ in range(4):
    t.forward(100)
    t.left(90)

turtle.done()
