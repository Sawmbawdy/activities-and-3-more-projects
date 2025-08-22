import turtle

turtle.Screen().bgcolor("black")
turtle.Screen().setup(800, 600)
t = turtle.Turtle()
side_length = 50
number_of_sides = 6
angle = 360.0 / number_of_sides

t.color("green")
for i in range(number_of_sides):
    t.right(angle)
    t.forward(side_length)
turtle.done()