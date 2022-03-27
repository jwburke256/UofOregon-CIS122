# CIS 122 Fall 2020 Assignment 2 Question 3
# Author: Jacob Burke
# Partner:
# References:
# https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php
# https://docs.python.org/3/library/math.html
# Description: Created two functions to help calculate the travel time in hours,
# minutes and seconds and then displays the results to the user

# Import the math module into python
import math

# Calculate travel time in minutes given the distance in miles and speed in mph
def calc_travel_time(distance, speed):
    travel_time = ((distance / speed) * 60)
    return travel_time


# Output the travel time hours, minutes and seconds given the distance and speed
def print_travel_time(distance, speed):
    print("To travel " + str(distance) + " miles at " + str(speed) + " MPH will take " + str(int(((distance/speed) * 60) / 60)) + " hr, " + str(int(((((distance/speed) * 60) / 60) % 1) * 60)) + " min and " + str(round(((((((distance/speed) * 60) / 60) % 1) * 60) % 1) * 60)) + " sec")

# Output the travel time hours, minutes and seconds given the distance = 120
# and speed = 55
print_travel_time(distance=120, speed=55)

# Output the travel time hours, minutes and seconds given the distance = 120
# and speed = 70
print_travel_time(distance=120, speed=70)

# Output the travel time hours, minutes and seconds given the distance = 5
# and speed = 25
print_travel_time(distance=5, speed=25)

# Output the travel time hours, minutes and seconds given the distance = 5
# and speed = 35
print_travel_time(distance=5, speed=35)
