""" Create a Turtle, name it, make it BLUE and draw a Smiley Face"""
import turtle
wn = turtle.Screen()
BLUE = turtle.Turtle()

BLUE.penup()
BLUE.goto(-75,150)
BLUE.pendown()
BLUE.circle(10)

BLUE.penup()
BLUE.goto(75,150)
BLUE.pendown()
BLUE.circle(10)

BLUE.penup()
BLUE.goto(0,0)
BLUE.pendown()
BLUE.circle(100,90)

BLUE.penup()
BLUE.goto(0,0)
BLUE.right(270)
BLUE.pendown()
BLUE.circle(-100,90)
l
input()
