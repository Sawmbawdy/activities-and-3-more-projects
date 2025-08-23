import turtle
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t.color("lime")
t.pensize(3)
t.speed(0.1)
for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()