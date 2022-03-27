# CIS 122 Fall 2020 Lab 8
# Author: Jacob Burke
# Partner: 
# Description: Created a set of functions. The first function will produce a set
# of random integers in a list. The following functions search and return values
# from the list such as high score, or median number. The final two functions
# are used to produce grade results from a list of integers.

import random

# Create Functions:
def gen_random_integer_list(num, start_range = 1, end_range = 100, sort_list = 'N'):
    '''
    Creates a list and adds random integers to it. The integers will be within
    numbers use as starting and ending integer values. The amount of random
    numbers added is determined by the num parameter. The function then returns
    the newly created list
    
    Extended Summary:
    Creates a list and adds random integers to it. The integers will be within
    numbers use as starting and ending integer values. The amount of random
    numbers added is determined by the num parameter. The function then returns
    the newly created list
    
    Args:
    num (int): file input
    start_range (int): word to be searched
    end_range (int): 
    sort_list (str): 

    Returns:
    t list with random numbers having been added to it
    '''
    #Create List variable
    t = []
    #Check num to make sure it is greater than 0
    if num <= 0:
      print('num must be > 0')
    #Check num to make sure it is an integer
    elif not isinstance(num, int):
      print('num must be an integer')
    #Check numbers input as range values
    elif not isinstance(start_range, int) or not isinstance(end_range, int):
      print('start_range and end_range must be integers')
    else:
        # Adds random numbers to the list. The # of numbers added is based off
        # the range value
        for i in range(num):
            r = random.randint(start_range, end_range)
            t.append(r)
        # Will sort the newly created lists integer values.
        if sort_list.upper() == 'Y':
            t.sort()

    return t

def get_high_score(t):
    '''
    Sorts a list and returns the highest integer value within it.
    
    Extended Summary:
    Sorts a list and returns the highest integer value within it. Prints errors
    if argument isn't a list or list is empty.
    
    Args:
    t (list): list

    Returns:
    returns the highest integer value from the list
    '''
    if not isinstance(t, list):
        print('List argument expected')
        return -1
    if len(t) == 0:
        return 0
    else:
        sorted_list = t[:]
        sorted_list.sort()
        return sorted_list[-1]

def get_low_score(t):
    '''
    Sorts a list and returns the lowest integer value within it.
    
    Extended Summary:
    Sorts a list and returns the lowest integer value within it. Prints errors
    if argument isn't a list or list is empty.
    
    Args:
    t (list): list

    Returns:
    returns the lowest integer value from the list
    '''
    if not isinstance(t, list):
        print('List argument expected')
        return -1
    if len(t) == 0:
        return 0
    else:
        sorted_list = t[:]
        sorted_list.sort()
        return sorted_list[0]

def get_mean_score(t):
    '''
    Produces the average number from a list of integers
    
    Extended Summary:
    Produces the average number from a list of integers. Prints errors
    if argument isn't a list or list is empty.
    
    Args:
    t (list): list

    Returns:
    returns the average number from a list of integers
    '''
    if not isinstance(t, list):
        print('List argument expected')
        return -1
    if len(t) == 0:
        return 0
    else:
        mean = sum(t) / len(t)
        return mean

def get_median_score(t):
    '''
    Produces the median number from a list of integers
    
    Extended Summary:
    Produces the median number from a list of integers. Prints errors
    if argument isn't a list or list is empty.
    
    Args:
    t (list): list

    Returns:
    returns the median number from a list of integers
    '''
    if not isinstance(t, list):
        print('List argument expected')
        return -1
    if len(t) == 0:
        return 0
    elif len(t) == 1:
        return t[0]
    else:
        if len(t) % 2 == 0:
            sorted_list = t[:]
            sorted_list.sort()
            first_middle_num = (len(sorted_list) / 2)
            first_middle_num = int(first_middle_num)
            second_middle_num = (len(sorted_list) / 2) + 1
            second_middle_num = int(second_middle_num)
            median_num = (sorted_list[first_middle_num] + sorted_list[second_middle_num]) / 2
            return median_num
        else:
            sorted_list = t[:]
            sorted_list.sort()
            middle_num = round(len(sorted_list) / 2)
            return t[middle_num]

def count_range(t, low_score, high_score):
    '''
    Counts the number of integers from a list between a given set of range
    parameters. Then it produces the number of integer values found within
    the given range.
    
    Extended Summary:
    Counts the number of integers from a list between a given set of range
    parameters. Then it produces the number of integer values found within
    the given range. Prints errors if list argument isn't a list, scores aren't
    integers, or if the starting score is higher than the end score, and vice
    versa.
        
    
    Args:
    t (list): list
    low_score (int): starting number for the range
    high_score (int): end number for the range
    
    Returns:
    Returns the number of integer values found within the given range.
    '''
    count = 0
    if not isinstance(t, list):
        print('List argument expected')
        return -1
    if isinstance(low_score, int) != True or isinstance(high_score, int) != True:
        print('start and end must be integers')
        return -1
    if low_score > high_score or low_score == high_score:
        print('start must be < end')
        return -1
    if len(t) == 0:
        return 0
    for i in t:
        if i >= low_score and i <= high_score:
            count += 1
    return count
        
def list_range(t):
    '''
    Utilizes the count_range function and prints the grade ranges from a list
    of scores that could range from 0 to 100. The results are shown as
    decreasing grades from As down to Fs, with the number of scores found
    within a list from each of the grade ranges.
    
    Extended Summary:
    Utilizes the count_range function and prints the grade ranges from a list
    of scores that could range from 0 to 100. The results are shown as
    decreasing grades from As down to Fs, with the number of scores found
    within a list from each of the grade ranges.
    
    Args:
    t (list): list

    Returns:
    None
    '''
    print('A - ' + str(count_range(t, 90, 100)))
    print('B - ' + str(count_range(t, 80, 89)))
    print('C - ' + str(count_range(t, 70, 79)))
    print('D - ' + str(count_range(t, 60, 69)))
    print('F - ' + str(count_range(t, 0, 59)))
    
t = gen_random_integer_list(100)
list_range(t)
