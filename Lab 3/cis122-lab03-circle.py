# CIS 122 Fall 2020 Lab 3
# Author: Jacob Burke
# Partner: 
# Description: Creates a specified number of concentric circles based on user
# inputed arguments

import turtle
t = turtle.Turtle()

def move(t, x, y):
    """
    Move Turtle to x, y position
    """
    t.pu()
    t.goto(x, y)
    t.pd()
    
def draw_circle(t, radius, x, y):
    """
    Draw a circle of length radius using Turtle t at position x, y
    """
    move(t, x, y - radius)
    t.circle(radius)

def draw_concentric_circles(n, s, gap, x, y):
    """
    Draws n number of circles with s = initial size(radius), gap = specified gap
    and x and y = starting point parameters
    """
    for i in range(n):
        draw_circle(t, s, x, y)
        s = s + gap

draw_concentric_circles(n=3, s=50, gap=25, x=0, y=0)


'''
# Original Code for drawing a circle without using the turtle module that does
  the same

# Import Turtle graphics module and create a turtle for drawing
import turtle
import math

# Sets up variables
bob = turtle.Turtle()
print(bob)

# function for drawing a polygon
def polygon(t, n, length):
        angle = 360 / n
        for i in range(n):
                t.fd(length)
                t.lt(angle)

# Fucntion that can draw a circle using a turtle and the polygon function
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)

# Calling a function using bob to draw a circle
circle(t=bob, r=70)
turtle.mainloop

----------------------------------------------------------------------------

# Practice code for drawing a concentric circles without using a function
# Importing turtle and creating turtle object
import turtle
t = turtle.Turtle()

# Draw three concentric circles
# Circle 1
radius = 50
t.circle(radius)
radius=50
t.pu();
t.rt(90);
t.fd(radius * 0.25)
t.lt(90)
t.pd()
t.circle(radius)

# Circle 2
radius = 75
t.pu();
t.rt(90);
t.fd(radius * 0.25);
t.lt(90)
t.pd()
t.circle(radius)

# Circle 3
radius = 100
t.pu();
t.rt(90);
t.fd(radius * 0.25);
t.lt(90)
t.pd()
t.circle(radius)
'''
