# CIS 122 Fall 2020 Assignment 6 Module
# Author: Jacob Burke
# Partner: 
# Description: Created functions to add padding to a data input. User can
# specify the size, direction that the padding extends out to, and the character
# itself to be used as padding.

# Create functions to be imported in another python file
def pad_string(data, size, direction = 'left', character = ' '):
    '''
    Takes a string and adds padding to either the left or right side of it

    Extended Summary:
    Takes a string and adds padding to either the left or right side of it. The
    padding size, which direction the padding extends out to, and the character
    to be used as padding can all be specified.

    Args:
    data (str): string input to add padding to on either side
    size (int): the length of the padding
    direction (str): which direction the padding extends out to. The default is
    to extend to the left
    character (str): the character to be used as padding

    Returns:
    Returns a formated string of the data input
    '''
    if len(data) > size:
        return str(data)
    if direction == 'left':
        formated_data = str(character*size) + str(data)
        return str(formated_data)
    elif direction == 'right':
        formated_data = str(data) + str(character*size)
        return str(formated_data)
    else:
        pass

def pad_left(data, size, character = ' '):
    '''
    Utilizes the pad_string function, while specifying the direction to be left

    Extended Summary:
    Utilizes the pad_string function, while specifying the direction to be left.
    The specification is done by changing the direction variable.
    
    Args:
    data (str): string input to add padding to on either side
    size (int): the length of the padding
    character (str): the character to be used as padding

    Returns:
    Returns a formated string of the data input
    '''
    direction = 'left'
    return pad_string(data, size, direction, character)


def pad_right(data, size, character = ' '):
    '''
    Utilizes the pad_string function, while specifying the direction to be right

    Extended Summary:
    Utilizes the pad_string function, while specifying the direction to be
    to the right. The specification is done by changing the direction variable.
    
    Args:
    data (str): string input to add padding to on either side
    size (int): the length of the padding
    character (str): the character to be used as padding

    Returns:
    Returns a formated string of the data input
    '''
    direction = 'right'
    return pad_string(data, size, direction, character)
