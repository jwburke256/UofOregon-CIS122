# CIS 122 Fall 2020 Lab 2
# Author: Jacob Burke
# Partner: 
# Description: Calculates the average amount of time in seconds light will
# take to reach the surface of the Earth and Pluto.

#Facts:
'''

    The speed of light is 186,282 miles per second (mps) in a vacuum.
    The average distance of the sun from the Earth is 93,000,000 miles.
    The average distance of the sun from Pluto is 3,670,050,000 miles.
'''

#Result:
'''
Output your solution using the round() function to set the number of decimal places to 2.
The output from your program must be in the following format, substituting xxx.xx and yyy.yy with the correct values from your calculation.
'''

#Establishing Variables:
#Speed of light in mps
spd_light = 186282
#Distance from sun to Earth in miles
earth_sun_dis = 93000000
#Distance from sun to Pluto in miles
pluto_sun_dis = 3670050000

#Original Code
#Function of lightyears from sun to earth, result is in seconds
def earth_sun_lightyear_sec():
    return earth_sun_dis / spd_light

#Function of lightyears from sun to pluto, result is in seconds
def pluto_sun_lightyear_sec():
    return pluto_sun_dis / spd_light

#Prints speed of light from sun to planets, rounded to 2 decimal places
print('Light travels from the sun to the Earth an average of', round(earth_sun_lightyear_sec(), 2), 'seconds.')
print('Light travels from the sun to Pluto an average of', round(pluto_sun_lightyear_sec(), 2), 'seconds.')


#New Code
#Fruitful function that calculates and returns the average time light takes to travel from the sun to an object at a given distance in miles.
def avg_light_travel_seconds (distance_miles):
    return round(distance_miles / spd_light, 2)

#Void function that outputs the results for each planetary object (Earth and Pluto)
def print_results(planetary_object, avg_light_travel_seconds, distance_miles):
    print(planetary_object, avg_light_travel_seconds(distance_miles), 'seconds.')

#Prints speed of light from sun to planets, rounded to 2 decimal places
print_results('Light travels from the sun to the Earth an average of', avg_light_travel_seconds, earth_sun_dis)
print_results('Light travels from the sun to Pluto an average of', avg_light_travel_seconds, pluto_sun_dis)
