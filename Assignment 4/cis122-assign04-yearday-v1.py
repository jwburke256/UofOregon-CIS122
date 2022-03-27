# CIS 122 Fall 2020 Assignment 4 Version 1 
# Author: Jacob Burke
# Partner: 
# Description: Used the is_leap_year function and typed a series of string and
# expressions to prompt the user for a day and year. It then outputs the month
# day and year as a string sentence.

# Copied over the is_leap_year function
def is_leap_year(n):
    '''
    Function that takes a year and calculates whether it's a leap year

    Extended Summary:
    Function that calculates if a given year is a leap year or not. This is
    through an algorithm that tests if the number is perfectly divisible by
    4, 100, and 400. Based on this, the function returns either a true or false
    value.

    Args:
    n (int): Year inputed

    Returns:
    Returns either true or false, to be used by test_is_leap_year() function
    '''
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# 1. Program opens and prompts the user to type in a year, and a day in that
#    year in that order (Must be integers, with the day being from 1-366),
#    also assigns values to variables

year = input('enter a year: \n')
year
year = int(year)
day = input('enter a day: \n')
day
day = int(day)
y = int(day)
month = 'avocado'

# 2. Program then uses the variables to determine if it is a leap year or
#    not using the is_leap_year function

x = int(year)
x = is_leap_year(x)
    
# 3. Flow of execution then branches to one of two conditional statements
#    based off of the leap_year function result
# 4. The After the pass through of the conditional statments, the values
#    assigned to the temporary variables of x and y then run through multiple
#    chained conidtionals, with relational operators, such as if 1 < x < 31
if x == True:
    if 1 <= day <= 31:
        month = 'January'
    elif 32 <= day <= 60:
        month = 'February'
        day = day - 31
    elif 61 <= day <= 91:
        month = 'March'
        day = day - 60
    elif 92 <= day <= 121:
        month = 'April'
        day = day - 91
    elif 122 <= day <= 152:
        month = 'May'
        day = day - 121
    elif 153 <= day <= 182:
        month = 'June'
        day = day - 152
    elif 183 <= day <= 213:
        month = 'July'
        day = day - 182
    elif 214 <= day <= 244:
        month = 'August'
        day = day - 213
    elif 245 <= day <= 274:
        month = 'September'
        day = day - 244
    elif 275 <= day <= 305:
        month = 'October'
        day = day - 274
    elif 306 <= day <= 335:
        month = 'November'
        day = day - 305
    elif 336 <= day <= 366:
        month = 'December'
        day = day - 335
    else:
        pass
else:
    if 1 <= day <= 31:
        month = 'January'
    elif 32 <= day <= 59:
        month = 'February'
        day = day - 31
    elif 60 <= day <= 90:
        month = 'March'
        day = day - 59
    elif 91 <= day <= 120:
        month = 'April'
        day = day - 90
    elif 121 <= day <= 151:
        month = 'May'
        day = day - 120
    elif 152 <= day <= 181:
        month = 'June'
        day = day - 151
    elif 182 <= day <= 212:
        month = 'July'
        day = day - 181
    elif 213 <= day <= 243:
        month = 'August'
        day = day - 212
    elif 244 <= day <= 273:
        month = 'September'
        day = day - 243
    elif 274 <= day <= 304:
        month = 'October'
        day = day - 273
    elif 305 <= day <= 334:
        month = 'November'
        day = day - 304
    elif 335 <= day <= 365:
        month = 'December'
        day = day - 334
    else:
        month = 'Error'
    
if x < 0:
    print("Year must be>0")
elif y < 0:
    print("Day of year must be >0")

if x == True and y >= 367:
    print("Day must be <= 366")
elif x == False and y >=366:
    print("Day must be <=365")


# 5. The conditional then ends, and another set of conditionals are used to
#   display the final results or the correct error messages
if x < 0:
    print("Year must be>0")
elif y < 0:
    print("Day of year must be >0")

if x == True and y >= 367:
    print("Day must be <= 366")
elif x == False and y >=366:
    print("Day must be <=365")

if x > 0 and y > 0 and (x == True and y < 367) or (x == False and y <366):
        print(str(month) + ' ' + str(day) + ', ' + str(year))
else:
    pass
