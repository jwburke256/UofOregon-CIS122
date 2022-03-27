# CIS 122 Fall 2020 Assignment 2 Question 1
# Author: Jacob Burke
# Partner:
# References:
# https://www.rapidtables.com/calc/math/pythagorean-calculator.html
# http://mathforum.org/dr.math/faq/faq.pythagorean.html
# https://docs.python.org/3/library/math.html
# Description: Calculates the missing side of a traingle with functions that use
# the Pythagorean Theorem

# Imports the math module into python
import math

def calc_side_c(a, b):
    '''
    Outputs side c of a triangle using the pythagoreon theorem equation with
    a = side a of triangle and b = side b of traingle.
    '''
    print("c = " + str(round(math.sqrt((math.pow(a, 2)) + (math.pow(b, 2))), 2)))

def calc_side_ab(ab, c):
    """
    Outputs either side a or b of a triangle using the pythagoreon theorem
    equation with a/b = either side a or b of a triangle and c = side c of
    a traingle.
    """
    print("a/b = " + str(round(math.sqrt((math.pow(c, 2)) - (math.pow(ab, 2))), 2)))

# Calculate missing side c
calc_side_c(a=5, b=10)

# Calculate missing side a or b
calc_side_ab(ab=4, c=8)

