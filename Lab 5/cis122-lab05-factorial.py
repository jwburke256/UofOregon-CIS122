# CIS 122 Fall 2020 Lab 4
# Author: Jacob Burke
# Partner: 
# Description: Create a set of user generated factorial functions. One that is
# the factorial function, and another function to test the first function. Then
# prompting a user to use the user generated factorial function and printing out
# the results.

# Importing Modules
import math

def factorial(num):
    '''
    Takaes a number and multiplies that number by itself and every number > 0
    below it

    Extended Summary:
    Takaes a number and multiplies that number by itself and every number > 0
    below it. If number is less than 0, it prints and error message and returns
    0. If the number is 0, it returns 1.

    Args:
    num (int): number input

    Returns:
    Returns the result of the factorial calculation
    '''
# Convert number to integer
    num = int(num)
# If number < 0 print error and return None
    if num < 0:
        print("Must be >= 0")
        return None
# If number < 0 print error and return None
    elif num == 0:
        return 1
# If number > 0
    else:
# Initialize total to 1
        total = 1
# Loop from 1 to number
        for i in range(1, num+1):
            total = total * i
# Return total
        return total

def test_factorial(num, show = False):
    '''
    Tests the user created factorial function against the math moduel function.

    Extended Summary:
    Tests the user created factorial function against the math moduel function.
    Has the option to display using a second argument the result of each
    individual loop comparison between the two functions tested. Displays an
    error message for each incorrect comparison of the functions. At the end of
    the function, it prints the total amount of errors, and the original number
    used in the function.

    Args:
    num (int): number input
    show (int): value used as an optional parameter

    Returns:
    Returns the the total amount of errors, and the original number
    used in the function as a printout for the user. If optional parameter is
    enabled, will also show each individual loop comparison.
    '''
    errors = 0
    range_num = num + 1
    total = 1
    for i in range(range_num):
        fact_result = factorial(i)
        mfact_result = math.factorial(i)
        if show == True:
          print(str(i) + ' : ' + str(fact_result) + ' ' + str(mfact_result))
        else:
            pass
        if fact_result != mfact_result:
            errors = errors + 1
            print('*' + str(fact_result) + ' ' + str(mfact_result))
        else:
            pass
        
    return print("Errors (" + str((num)) + '): ' + str(errors))
    
# Prompting user for input and printing result using function:
user_input = input("Enter factorial number: ")
user_input
user_input = int(user_input)
print(factorial(user_input))


# Testing Functions
# test_factorial(5, 1)


