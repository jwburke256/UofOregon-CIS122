# CIS 122 Fall 2020 Assignment 3 Question 2
# Author: Jacob Burke
# Partner: 
# Description: Function that takes a single integer and prints out a integer by
# integer grid of numbers

# Creating the void function using 2 loops
def draw_grid(n):
    """ Makes a NumberxNumber grid, with number being the argument.

    Extended summary:
    Draws a number by number grid based on the inputed argument. Makes a row
    first starting from 1 and ending in the argument number, then repeats the
    row below by the argument  inputed.

    Args:
    n (data type of param 1 and 2): user inputed number that creates the grid
    """
    for i in range(n):
        numbers = ''
        for x in range(1, n + 1):
            numbers = numbers + str(x) + ' '
        print(numbers)



# Testing the grid with the number 4
draw_grid(4)

