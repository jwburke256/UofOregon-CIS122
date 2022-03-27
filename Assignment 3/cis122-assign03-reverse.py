# CIS 122 Fall 2020 Assignment 3 Question 1
# Author: Jacob Burke
# Partner: 
# Description: Creating a function that takes a string as an argument, reversing
# it's word order, then returning it as a string back to where the function
# was called

# Creating Function
def reverse(string):
    """Takes a string and reversing it's word order

    Extended Summary
    A fucntion that takes a string as an argument, then reverses it. This is
    done by looping through. For example, taking the first letter as the first
    loop, then taking the second letter and adding the first loop letter after
    the second letter.

    Args:
    string (string): sentence inputer as an argument to be reversed

    Returns:
    reverse variable (string)
    """    
    original = string
    reverse = ''
    for letter in string:
        '''
        The expression below is making reverse the first letter, then taking
        the second letter, and adding the first letter AFTER the second letter,
        then repeating as such (because it is letter + reverse, instead of
        reverse + letter)
        '''
        reverse = letter + reverse
    return reverse

# Testing Function by printing orignal string then using a function on the it
print('When in the Course of human events')
print(reverse('When in the Course of human events'))

