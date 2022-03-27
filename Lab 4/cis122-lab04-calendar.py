# CIS 122 Fall 2020 Lab 4
# Author: Jacob Burke
# Partner: 
# Description: Created 4 functions. The first function takes an integer an input
# and outputs what corresponding month the integer goes to. The second function
# loops the first function, to print out all available months and demonstrates
# if an incorrect integer is used. The third function calculates if a year given
# is a leap year, by returning the value as either true or false. The fourth
# function takes the true or false value, as well as adding additional arguments
# being able to be used to loop multiple years. The true or false values are
# used to print whether a year is a leap year or not.

# Importing modules
import math

# Defining Functions
def get_full_month(n):
    '''
    Takaes a number and outputs the corresponding month.

    Extended Summary:
    Takes a nunmber between 1 and 12 and outputs the corresponding month. If the
    number given falls outside of that range, an error message is printed

    Args:
    n (int): month input

    Returns:
    Returns either the numbers corresponging month, or an error message
    displaying the incorrect value to the user.
    '''
    if n == 1:
        month = "January"
    elif n == 2:
        month = "February"
    elif n == 3:
        month = "March"
    elif n == 4:
        month = "April"
    elif n == 5:
        month = "May"
    elif n == 6:
        month = "June"
    elif n == 7:
        month = "July"
    elif n == 8:
        month = "August"
    elif n == 9:
        month = "September"
    elif n == 10:
        month = "October"
    elif n == 11:
        month = "November"
    elif n == 12:
        month = "December"
    elif n < 0 or n > 12:
        month = ""
    if 0 < n < 13:
        return print('The month is ' + month)
    else:
        return print('Must be an integer between 1 and 12 (' + str(n) + ' is invalid)')
    # return print('Must be an integer between 1 and 12 (' + str(n) + ' is invalid)')

def test_get_full_month():
    '''
    Function that tests the get_full_month function by looping it a total of 14
    times, starting with 0 and ending with 13

    Args:
    None

    Returns:
    Returns all possible months, as well as demonstrating the numbers zero and
    thirteen and the error message that corresponds to those values
    '''
    for i in range(14):
        get_full_month(i)

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


def test_is_leap_year(start_year, end_year):
    '''
    Function that lists multiple years and whether or not they are leap years.

    Extended Summary:
    Input two years to calculate the range that the function outputs. The
    function then uses the is_leap_year() function to calculate each year within
    the range, and then displays whether each year is or is not a leap year.

    Args:
    start_year (int): Starting year input used to calculate the starting point
                      of the range
    end_year (int): Ending year input used to calculate the ending point of the
                    range, with the output displaying that final year included

    Returns:
    Outputs all years within the given years used as the arguments, to include
    displaying the last year as the stopping point. Prints a message for each
    year if it is or is not a leap year.
    '''
    for i in range(start_year, end_year + 1):
        is_leap_year(i)
        if is_leap_year(i) == True:
            print('The year ' + str(i) + ' is a leap year (it has 366 days).')
        else:
            print('The year ' + str(i) + ' is not a leap year (it has 365 days).')





# Testing Function
test_is_leap_year(1996, 2112)
