# Star-and-big-star-by-turtle

#importing packages
import turtle
import math
import random

#Setting a screen
wn = turtle.Screen()
wn.title("By Lakshay Mahajan")

# Star and big star

lakshay = turtle.Turtle()
lakshay.getscreen().bgcolor("#994444")
lakshay.speed(20)

lakshay.penup()
lakshay.goto((-200, 100))
lakshay.pendown()

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for j in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
        turtle.end_fill()

star(lakshay, 360)



turtle.done()
