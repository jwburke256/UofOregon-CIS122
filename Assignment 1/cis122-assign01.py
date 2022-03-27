# CIS 122 Fall 2020 Assignment 1 
# Author: Jacob Burke 
# Credit: 
# Description: Introduction to programming problem set uses Python numeric data types and 
# operations to solve a variety of small problems.

#
# Question 1
#

print("Question 1")
print("------------------------------------------")

# Calculate the number of watermelons given 120 children at 3 slices
# 130 adults at 2 slices, 15 slices per watermelon, add 20% extra, rounding up.

import math

# Initialize variables with values
adults = 130
children = 120
slices_per_adult = 2
slices_per_child = 3
slices_per_watermelon = 15
extra = 0.2

# Calculate total number of watermelon slices and display number of slices
total_slices = (children * slices_per_child) + (adults * slices_per_adult)
print("Total slices:", total_slices)

# Add extra amount and display number of slices
total_slices = total_slices + (total_slices * extra)
print("Total slices (including extra):", total_slices)

# Calculate number of watermelons and display number of watermelons
watermelons = total_slices / slices_per_watermelon
print("Total watermelons:", watermelons)

# Round the number of watermelons up and display number of watermelons
watermelons = math.ceil(watermelons)
print("Total watermelons (rounded up):", watermelons)

#
# Question 2
#

print("Question 2")
print("------------------------------------------")

# Calculate total number of trips given 100, 500, 1000 or 5000 daily steps, 16
# steps per floor, and down and back up the stairs as one trip. Re-use the
# step variable. Round the number of trips up to the nearest whole integer.
# Recommended variable names: steps_per_floor, target_steps, trips

# Initialize variables
steps_per_floor = 16
floor = 5
target_steps = 1
one_trip = steps_per_floor * floor *2
trips = math.ceil(target_steps / one_trip)

# Calculate 100 steps and display number of trips
target_steps = 100
trips = math.ceil(target_steps / one_trip)
print("100 steps:", trips)

# Calculate 500 steps and display number of trips
target_steps = 500
trips = math.ceil(target_steps / one_trip)
print("500 steps:", trips)

# Calculate 1000 steps and display number of trips
target_steps = 1000
trips = math.ceil(target_steps / one_trip)
print("1000 steps:", trips)

# Calculate 5000 steps and display number of trips
target_steps = 5000
trips = math.ceil(target_steps / one_trip)
print("5000 steps:", trips)



#
# Question 3
#
      
print()
print("Question 3")
print("------------------------------------------")

# Calculate total distance walked per week given a pivot radius of 90 feet,
# five pivots, two inspections per day, and working five days a week. Round
# all results to two decimal places. Use 3.14, or math.pi, for the circumference
# equation calculation.

# Initialize variables
radius = 90
total_pivot_systems = 5
daily_inspection = 2
days_inspected_per_week = 5

# Calculate circumference of one pivot
one_pivot = 2 * math.pi * radius

#Calculate Weekly Distance in both feet and miles
weekly_distance_feet = (one_pivot * total_pivot_systems * daily_inspection * days_inspected_per_week)
weekly_distance_miles = (one_pivot * total_pivot_systems * daily_inspection * days_inspected_per_week) / 5280

# Calculate and display total distance walked (feet and miles)
print("Weekly distance (feet):", round(weekly_distance_feet, 2))
print("Weekly distance (miles):", round(weekly_distance_miles, 2))
