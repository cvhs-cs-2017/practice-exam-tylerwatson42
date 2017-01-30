"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""
import turtle
turtle.color("orange")
sven = turtle.Turtle()
for i in range(50):
    sven.forward(50)
    sven.left(123)

sven.color("pink")
for i in range(50):
    sven.forward(100)
    sven.left(123)
