# CIS 122 Fall 2020 Lab 2
# Author: Jacob Burke
# Partner: 
# Description: Create a function that returns the square of any positive integer

# Define a function that accepts a number

def square(num):
    # Verify the number is a positive integer (we will not be able to code this step yet)
    # Return the result of multiplying the parameter by itself (refactoring)
    return num * num

# assigns string to print variable, which makes the proper format for the final output
str_to_print = str(square(2)) + ', ' + str(square(10)) + ', ' + str(square(100))

# Test 2, 10, and 100, by printing string to print variable
print(str_to_print)

