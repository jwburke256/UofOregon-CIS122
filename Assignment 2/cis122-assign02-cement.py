# CIS 122 Fall 2020 Assignment 2 Question 2
# Author: Jacob Burke
# Partner:
# References:
# https://www.concretenetwork.com/concrete/howmuch/calculator.htm
# https://todayshomeowner.com/cubic-yard-calculator/
# https://docs.python.org/3/library/math.html
# Description: Calculates the amount of cement that is input in inches and
# prints results in cubic yards

# Import the math module into python
import math

# Return cement amount in yards using cubic inches given thickness (t), width
# (w) and length (l) in cubic inches
def calc_yards_cement(t, w, l):
    yards_cement = (round(((t / 12) * (w / 12) * (l / 12)) / 27, 2))
    return yards_cement

# Output (print) results of calculating yards given thickness (t), width (w) and
# length (l) in cubic inches
def print_results(t, w, l):
    print("A cement slab " + str(t) + '" thick, ' + str(w) + '" wide and ' + str(l) + '" long requires ' + str(calc_yards_cement(t, w, l)) + ' cubic yards of cement')

# Output (print) results of calculating yards given thickness (t) = 4,
# width (w) = 48, and length (l) = 144 in cubic inches
print_results(t=4, w=48, l=144)

# Output (print) results of calculating yards given thickness (t) = 4,
# width (w) = 180, and length (l) = 240 in cubic inches
print_results(t=4, w=180, l=240)
