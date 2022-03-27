# CIS 122 Fall 2020 Assignment 6
# Author: Jacob Burke
# Partner: 
# Description: Program prompts the user for a file to scan through. Once file
# is submitted, the program checks each line in the file. Results are printed
# that displays the number of integer lines, number of comment lines, sum of
# all integers, and the average integer, rounded to 2 decimal places. The
# program then reprompts the user for a new file. If no file is given the
# program ends.

# Import modules
from cis122_assign06_shared import pad_left, pad_right
import os

# Create Functions
def parse_random_numbers_file():
    '''
    Prompts the user for a file to scan through. Once file is submitted, the
    function checks each line in the file. Results are printed that displays
    the number of integer lines, number of comment lines, sum of all integers,
    and the average integer, rounded to 2 decimal places. The function then
    reprompts the user for a new file.

    Extended Summary:
    Prompts the user for a file to scan through. The function checks to see
    if the user put in a file name, and if not the function ends. If the file
    name is incorrect, the program notifies the user and reprompts them to
    try again. Once file is submitted, the function checks each line in the
    file. Results are printed that displays the number of integer lines, number
    of comment lines, sum of all integers, and the average integer, rounded to 2
    decimal places. The function then reprompts the user for a new file.

    Args:
    None

    Returns:
    None
    '''
    while True:
        text_file = input('Enter a filename (blank to exit): ')
        text_file = text_file.strip()
        if len(text_file) == 0:
            # Exit if nothing entered
            break
        elif not os.path.exists(text_file) == True:
            print("Invalid filename: " + str(text_file))
        else:
            fin = open(text_file)
            int_count = 0
            line_comment = 0
            sum_of_int = 0
            for line in fin:
                if line.strip()[0] == '#':
                    line_comment = line_comment + 1
                else:
                    int_count = int_count + 1
                    sum_of_int = sum_of_int + int(line.strip())
                    
            # Close file
            fin.close()
            # Variables for pad_left and pad_right
            label_spacing = 11
            num_spacing = 10
            # Print results
            print(pad_right("Count: ", label_spacing) + str(int_count))
            print("Comments: " + pad_left((str(line_comment)), num_spacing))
            print("Total: " + pad_left(str(sum_of_int), num_spacing))
            print("Average: " + pad_left(str((round((sum_of_int / int_count), 2))), 7))


# Execute Function:
parse_random_numbers_file()
