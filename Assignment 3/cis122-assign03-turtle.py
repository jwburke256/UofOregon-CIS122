# CIS 122 Fall 2020 Assignment 3 Question 3
# Author: Jacob Burke
# Partner: 
# Description: Created 3 functions. The first function draws a line using turtle
# graphics, the second function utilizes the first function to draw a radial,
# and the final function draws 4 radials, each separated evenly in their own
# quadrants.

# Importing Modules
import math
import turtle

t = turtle.Turtle()

# Creating Functions
def draw_line(t, x, y, angle, length):
    """Draws a line using turtle graphics based on the functionsarguments

Draws a line based on the arguments inputed into the function. The turtle in the
function starts in the up position, moves to the x and y location based off the
second and third argument, rotates towards the angle based on the fourth
argument, puts the pen down, draws a line with the distance based off the fifth
argumet, and then picks the pen back up, ready to have another line drawn again
by repeating the argument.

Args:
   t (Turtle): Drawing Turtle
   x (int/float): starting x location
   y (int/float): starting y location
   angle (int/float): moves the turtles facing direction towards the angle input
                      in degrees
   length (int/float): draws a line measured in pixels from the argument
Returns:
      None
    """
    t.pu()
    t.setx(x)
    t.sety(y)
    t.seth(angle)
    t.pd()
    t.fd(length)
    t.pu()

def draw_radial_lines(t, x, y, length, num_lines):
    """Draws radial lines in a 360 degree pattern, each ray evenly spaced

Extended summary: Draws radial lines in a 360 degree pattern, with each ray
being evenly spaced out. This is done by the user inputing the turtle argument,
starting location on the x and y axis, length of each ray, and the number of
lines (or rays). The number of lines is used to calculate the angle to make an
evenly spaced distance between each ray out of 360 degrees, to make a circular
pattern. Uses the draw_line function within to draw each ray.

Args:
t (Turtle): Drawing Turtle
x (int/float): starting x location
y (int/float): starting y location
length (int/float): draws a line measured in pixels from the argument
num_lines (int/float): number of rays drawn, used to calculate the offset of
                       the angles for each ray

Returns:
None
"""
    changing_angle = 0
    for i in range(num_lines):
        starting_angle = 360 / num_lines
        changing_angle = changing_angle + starting_angle
        draw_line(t, x , y, changing_angle, length)


def draw_radials_in_quadrants(t, length, num_lines):
    """draws multiple radials around 4 quadrants, each spaced apart evenly

Extended Summary:
Uses the draw_radial_lines function 4 times to draw 4 radials in their own
separate quadrants, with the distance between each radial as 2 times the
inputed length of each ray. 

Args:
t (Turtle): Drawing Turtle
length (int/float): used to calculate both the length of each ray, as well as
                    the distance between each radial
num_lines (int/float): number of rays drawn per radial, used to calculate
                       the offset of the angles for each ray


Returns:
None
"""
    draw_radial_lines(t, 2*length, 2*length, length, num_lines)
    draw_radial_lines(t, -2*length, 2*length, length, num_lines)
    draw_radial_lines(t, -2*length, -2*length, length, num_lines)
    draw_radial_lines(t, 2*length, -2*length, length, num_lines)

# Final Test
# draw_radials_in_quadrants(t, 75, 8)
draw_radials_in_quadrants(t, 50, 16)

# 1st Test
# draw_line(t, 100, 100, 0, 200)
# draw_line(t, -100, -100, 270, 50)
# draw_line(t, 200, -200, 45, 75)

# 2nd Test
# draw_radial_lines(t, -100, -100, 25, 8)
# draw_radial_lines(t, -100, 100, 100, 4)
# draw_radial_lines(t, 100, -100, 200, 16)
# draw_radial_lines(t, 100, 100, 50, 32)
