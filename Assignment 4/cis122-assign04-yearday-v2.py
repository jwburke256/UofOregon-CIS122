# CIS 122 Fall 2020 Assignment 4 Version 2 
# Author: Jacob Burke
# Partner: 
# Description: Copied over the is_leap_year function and the algorithm in the
# v1 file. Then through a process of refactoring, created a set of functions.
# Then made a final function that utilizes the earlier functions to prompt the
# user for a day and year. It then outputs the month day and year as a string
# sentence.

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

# Creating New Functions through a process of refactoring the v1 file
def valid_year(year):
    '''
    Function that validates the year being input is a correct value

    Extended Summary:
    Function that validates the year being input is a correct value

    Args:
    year (int): Year input

    Retruns:
    Returns either False if the year is incorrect, or True if correct
    '''
    year = int(year)
    if year < 0:
        print("Year must be > 0")
        return False
    else:
        return True

# print(bool(valid_year(2020)))


def valid_day_of_year(year, day_of_year):
    '''
    Function that takes a year and calculates whether it's a leap year

    Extended Summary:

    Args:
    year (int): Year inputed used to see if leap year should be accounted for
    day_of_year (int): day input

    Returns:
    Returns either False if day input is incorrect, or True if correct
    '''

    if day_of_year < 0:
        print("Day of year must be >0")
        return False
    elif day_of_year == 0:
        print("Day cannot be zero")
        return False
    elif is_leap_year(year) == True and day_of_year >= 367:
        print("Day must be <= 366")
        return False
    elif is_leap_year(year) == False and day_of_year >=366:
        print("Day must be <=365")
        return False
    else:
        return True

# print(bool(valid_day_of_year(2019, 368)))

def input_year():
    '''
    Function that prompts the user for a year and returns the year as an integer.

    Extended Summary:
    Function that prompts the user for a year. If year is incorrect, function
    returns 0. If correct it returns the year value as an integer

    Args:

    Returns:
    If year is incorrect, function returns 0. If correct it returns the year
    value as an integer
    '''
    year = input('enter a year: \n')
    year = int(year)
    if valid_year(year) == False:
        return 0
    elif year == 0:
        print("Year cannot be 0")
        return 0
    else:
        return year

# print(str(input_year()))

def input_day_of_year(year):
    '''
    Function that prompts the user for a day of the year and returns the day as
    an integer

    Extended Summary:
    Function that prompts the user for a day of the year. If year input into
    function is incorrect, it returns 0. If day of year is incorrect, it
    returns 0. If year input into function, and user input of day of year is
    correct, then the function returns the day of the year as an integer.

    Args:
    year (int): Year input that is checked against the valid_year function

    Returns:
    If year input into function is incorrect, it returns 0. If day of year
    is incorrect, it returns 0. If year input into function, and user input
    of day of year is correct, then the function returns the day of the year
    as an integer.
    '''
    day_of_year = input('enter a day: \n')
    day_of_year = int(day_of_year)
    if valid_year(year) == False:
        return 0
    elif valid_day_of_year(year, day_of_year) == False:
        return 0
    elif day_of_year == 0:
        print("Day cannot be 0")
        return 0
    else:
        return day_of_year

# print(bool(input_day_of_year(2020)))

def get_days_in_year(year):
    '''
    Function that takes a year and outputs how many days are in the year.

    Extended Summary:
    Function takes a year. If the year is invalid it returns 0. Function then
    checks to see if the year is a leap year, and depending on true or false
    result, it will return the correct amount of days for that year as an int.

    Args:
    year (int): Year input that is used to determine if leap year or not

    Returns:
    If the year is invalid it returns 0. Function then checks to see if the
    year is a leap year, and depending on true or false result, it will return
    the correct amount of days for that year as an int.
    '''
    days_in_year = 1
    if valid_year(year) == False:
        return 0
    elif year == 0:
        print("Year cannot be 0")
        return 0
    elif is_leap_year(year) == True:
        days_in_year = int(366)
        return days_in_year
    elif is_leap_year(year) == False:
        days_in_year = int(365)
        return days_in_year
    else:
        return 0

# print(str(get_days_in_year(2019)))

def valid_month(month):
    '''
    Function that takes a month as an intger between 1 and 12 and determines
    if it is correct or not.

    Extended Summary:
    Function takes a month, and converts it to an integer. If the number is less
    than or equal to 0 it prints an error massage and returns as false.
    If the month is greater than 12 it prints and error message and returns as
    false. If the month is correct it returns as true.

    Args:
    month (int): Month input

    Returns:
    If the number is less than or equal to 0 it prints an error massage and
    returns as false. If the month is greater than 12 it prints and error
    message and returns as false. If the month is correct it returns as true.
    '''
    month = int(month)
    if month < 0:
        print("Month must be > 0")
        return False
    elif month > 12:
        print("Month must be <= 12")
        return False
    elif month == 0:
        print("Month cannot be 0")
    else:
        return True

# print(bool(valid_month(0)))

def translate_month(month):
    '''
    Function that takes a month as an integer and outputs the corresponding
    English name of the month as a string.

    Extended Summary:
    Function takes a month, and converts it to an integer. Then it checks to
    see if the month input is correct. If not it returns as an empty string.
    If month is correct, it then runs a set of conditional statements to
    determine the correct corresponding month's english name, and returns that
    name as a string.

    Args:
    month (int): Month inputed

    Returns:
    Returns an empty string if incorrect month is input. If correct value, the
    corresponding english name for the month is output as a string.
    '''
    month = int(month)
    if valid_month(month) == False:
        return ''
    elif valid_month(month) == True:
        if month == 1:
            month = 'January'
            return month
        elif month == 2:
            month = 'February'
            return month
        elif month == 3:
            month = 'March'
            return month
        elif month == 4:
            month = 'April'
            return month
        elif month == 5:
            month = 'May'
            return month
        elif month == 6:
            month = 'June'
            return month
        elif month == 7:
            month = 'July'
            return month
        elif month == 8:
            month = 'August'
            return month
        elif month == 9:
            month = 'September'
            return month
        elif month == 10:
            month = 'October'
            return month
        elif month == 11:
            month = 'November'
            return month
        elif month == 12:
            month = 'December'
            return month
        else:
            month = 'Error'
            return month
    else:
        print('Error')

# print(translate_month(12))

def get_days_in_month(year, month):
    '''
    Function that takes a year and month and then outputs the amount of days
    in that month as an integer.

    Extended Summary:
    Function takes a year and month as arguments. It then uses a conditional
    execution to determine whether or not the year argument is a leap year.
    Flow of execution then branches, and then uses multiple chained conditionals
    to check the month value and outputs the number of days in the month as an
    integer

    Args:
    year (int): Year inputed
    month (int): Month inputed

    Returns:
    Returns the amount of days in that particular month and year provided as an
    integer.
    '''
    if is_leap_year(year) == True:
        if month == 1:
            days = 31
            return int(days)
        elif month == 2:
            days = 29
            return int(days)
        elif month == 3:
            days = 31
            return int(days)
        elif month == 4:
            days = 30
            return int(days)
        elif month == 5:
            days = 31
            return int(days)
        elif month == 6:
            days = 30
            return int(days)
        elif month == 7:
            days = 31
            return int(days)
        elif month == 8:
            days = 31
            return int(days)
        elif month == 9:
            days = 30
            return int(days)
        elif month == 10:
            days = 31
            return int(days)
        elif month == 11:
            days = 30
            return int(days)
        elif month == 12:
            days = 31
            return int(days)
        else:
            days = 0
            return days
    if is_leap_year(year) == False:
        if month == 1:
            days = 31
            return int(days)
        elif month == 2:
            days = 28
            return int(days)
        elif month == 3:
            days = 31
            return int(days)
        elif month == 4:
            days = 30
            return int(days)
        elif month == 5:
            days = 31
            return int(days)
        elif month == 6:
            days = 30
            return int(days)
        elif month == 7:
            days = 31
            return int(days)
        elif month == 8:
            days = 31
            return int(days)
        elif month == 9:
            days = 30
            return int(days)
        elif month == 10:
            days = 31
            return int(days)
        elif month == 11:
            days = 30
            return int(days)
        elif month == 12:
            days = 31
            return int(days)
        else:
            days = 0
            return days

# print(get_days_in_month(year=2019, month=0))

def valid_day(year, month, day):
    '''
    Function that takes a year, month, and day and verifies that the they are
    correct values.

    Extended Summary:
    Function that takes a year, month, and day and verifies that the they are
    correct values. If any values are incorrect it returns False. If correct
    it returns True. It utilizes 3 functions that individually check each
    parameter one by one.

    Args:
    year (int): Year inputed
    month(int): Month inputed
    day (int): Day inputed

    Returns:
    If any values are incorrect it returns False. If correct it returns True.
    '''
    if valid_year(year) == True:
        if valid_day_of_year(year, day) == True:
            if valid_month(month) == True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# print(bool(valid_day(2020, 12, 28))) (doesn't take into account days over 31)

def get_date_string(year, month, day):
    '''
    Function that takes a year, month, and day as integer values and outputs
    them as a sentence by combining multiple strings.

    Extended Summary:
    Function takes three integer arguments, being a year, month, and day
    respectively. It uses the valid_day function to check to make sure that
    each argument is a valid value. It then makes a variable and assigns the
    day of that specific month using the day_of_month function. From there
    it utilizes multiple functions to convert each intger value one by one
    into it's corresponding string if neccesary. The function then combines
    each value into a sentence and outputs the sentence as a print statement.

    Args:
    year (int): Year inputed
    month(int): Month inputed
    day (int): Day inputed

    Returns:
    Returns the corresponding year day and month as a print statement.
    '''
    if valid_day(year, month, day) == True:
        day_of_month = get_day_of_month(year, day)
        string_year = str(year)
        string_month = translate_month(month)
        string_day = str(day_of_month)
        string_statement = print(string_month + ' ' + string_day + ', ' + string_year)
        return string_statement
    else:
        return ''

# get_date_string(year=2020,month=2,day=29)

def get_month(year, day):
    '''
    Function that takes a year and day as integer values and outputs
    the corresponding month that matches up with them.

    Extended Summary:
    Function that takes a year and day as integer values. The year is then input
    into the is_leap_year function in a conditional. Flow of execution then
    diverges based off this, and nested conditionals with relational operators
    are used to determine exactly what month correlates with the day value
    input. The Function then outputs the month as an integer.

    Args:
    year (int): Year inputed
    day (int): Day inputed

    Returns:
    month as an integer value
    '''
    if is_leap_year(year) == True:
        if 1 <= day <= 31:
            month = 1
            return month
        elif 32 <= day <= 60:
            month = 2
            return month
        elif 61 <= day <= 91:
            month = 3
            return month
        elif 92 <= day <= 121:
            month = 4
            return month
        elif 122 <= day <= 152:
            month = 5
            return month
        elif 153 <= day <= 182:
            month = 6
            return month
        elif 183 <= day <= 213:
            month = 7
            return month
        elif 214 <= day <= 244:
            month = 8
            return month
        elif 245 <= day <= 274:
            month = 9
            return month
        elif 275 <= day <= 305:
            month = 10
            return month
        elif 306 <= day <= 335:
            month = 11
            return month
        elif 336 <= day <= 366:
            month = 12
            return month
        else:
            month = 0
            return month
    else:
        if 1 <= day <= 31:
            month = 1
            return month
        elif 32 <= day <= 59:
            month = 2
            return month
        elif 60 <= day <= 90:
            month = 3
            return month
        elif 91 <= day <= 120:
            month = 4
            return month
        elif 121 <= day <= 151:
            month = 5
            return month
        elif 152 <= day <= 181:
            month = 6
            return month
        elif 182 <= day <= 212:
            month = 7
            return month
        elif 213 <= day <= 243:
            month = 8
            return month
        elif 244 <= day <= 273:
            month = 9
            return month
        elif 274 <= day <= 304:
            month = 10
            return month
        elif 305 <= day <= 334:
            month = 11
            return month
        elif 335 <= day <= 365:
            month = int(12)
            return month
        else:
            month = 0
            return month

def get_day_of_month(year, day):
    '''
    Function that takes a year and day as integer values and outputs
    the exact day in the month calculated off of the larger day value.

    Extended Summary:
    Function that takes a year and day as integer values. It then uses a
    branching conditional to change the flow of exection by running the is_leap
    _year function. From there is runs a set of nested conditionals that
    use relational operators to determine if the day value falls within it's
    field. If the value does, it adjusts the day value to be the correct day
    amount within that specific month it would fall into, then returns that
    value.

    Args:
    year (int): Year inputed
    day (int): Day inputed

    Returns:
    exact day value as an integer
    '''

    if is_leap_year(year) == True:
        if 1 <= day <= 31:
            return day
        elif 32 <= day <= 60:
            day = day - 31
            return day
        elif 61 <= day <= 91:
            day = day - 60
            return day
        elif 92 <= day <= 121:
            day = day - 91
            return day
        elif 122 <= day <= 152:
            day = day - 121
            return day
        elif 153 <= day <= 182:
            day = day - 152
            return day
        elif 183 <= day <= 213:
            day = day - 182
            return day
        elif 214 <= day <= 244:
            day = day - 213
            return day
        elif 245 <= day <= 274:
            day = day - 244
            return day
        elif 275 <= day <= 305:
            day = day - 274
            return day
        elif 306 <= day <= 335:
            day = day - 305
            return day
        elif 336 <= day <= 366:
            day = day - 335
            return day
        else:
            day = 0
            return day
    else:
        if 1 <= day <= 31:
            return day
        elif 32 <= day <= 59:
            day = day - 31
            return day
        elif 60 <= day <= 90:
            day = day - 59
            return day
        elif 91 <= day <= 120:
            day = day - 90
            return day
        elif 121 <= day <= 151:
            day = day - 120
            return day
        elif 152 <= day <= 181:
            day = day - 151
            return day
        elif 182 <= day <= 212:
            day = day - 181
            return day
        elif 213 <= day <= 243:
            day = day - 212
            return day
        elif 244 <= day <= 273:
            day = day - 243
            return day
        elif 274 <= day <= 304:
            day = day - 273
            return day
        elif 305 <= day <= 334:
            day = day - 304
            return day
        elif 335 <= day <= 365:
            day = day - 334
            return day
        else:
            day = 0
            return day

    
def start():
    '''
    Function that takes a user input year and day value, then prints out the
    month, day, and year as a sentence.

    Extended Summary:
    Function that takes a user input year and day value. From there it
    calculates the missing month and the exact day value that would fall into
    the month. This is done using the get_month function. It then runs the
    get_date_string function to print out the results, while at the same time
    verifying that the arguments are valid.
    
    Args:


    Returns:
    prints out the month, day, and year as a sentence from the user inputed
    values.
    '''
# Get year input
    year = input_year()
    year
    year = int(year)
# Get day input
    day = input_day_of_year(year)
    day
    day = int(day)
    y = int(day)
    x = int(year)
# Get month using year and day input
    month = get_month(year, day)
# Print results
    get_date_string(year, month, day)
    
start()
