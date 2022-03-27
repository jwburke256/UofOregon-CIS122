# CIS 122 Fall 2020 Assignment 7
# Author: Jacob Burke
# Partner: 
# Description: Created a set of functions that allow a user to make a list of
# items. The user is prompted to input commands, with a help command that
# will list the available command options. From there the user can add to and
# delete items from a list of their choosing. They can also list the items that
# they add to the list

# Create functions:
def cmd_help():
    print('*** Available commands ***')
    cmds = ['Add', 'Delete', 'List', 'Clear']
    cmds_desc = ['Add to list', 'Delete information', 'List informtation', 'Clear list']
    for i in range(len(cmds)):
        print(pad_right(str(cmds[i]), get_max_list_item_size(cmds) + 5) + str(cmds_desc[i]))
    print('Empty to exit')
    return
    
def cmd_add(t):
    while True:
        new_item = input("Enter the information (empty to stop): ")
        new_item = new_item.strip()
        if len(new_item) > 0:
            t.append(new_item)
            print("Added, item count = " + str(len(default_list)))
        else:
            return False
    return      

def cmd_delete(t):
    print("List contains " + str(len(t)) + ' item(s)')
    if len(t) == 0:
        return
    else:       
        for i in range(len(t)):
            print(pad_right(str(i), 3) + t[i])
        while True:
            del_num = input("Enter number to delete (empty to stop): ")
            del_num = del_num.strip()
            if del_num == '':
                return False
            elif del_num.isdigit() != True:
                print("Must be a valid integer")
            else:
                del_num = int(del_num)
                if 0 <= del_num <= len(t):
                    del t[del_num]
                    if len(t) == 0:
                        print("All items deleted")
                        return False
                    else:
                        for i in range(len(t)):
                            print(pad_right(str(i), 3) + t[i])
                else:
                    print("Must be a integer # between 0 and " + str(len(t)))
        return

def cmd_list(t):
    print("List contains " + str(len(t)) + ' item(s)')
    for i in range(len(t)):
        print(t[i])

def cmd_clear(t):
    prior_size = len(t)
    t.clear()
    print(str(prior_size) + " item(s) removed, list empty")

def get_max_list_item_size(t):
    item_size = 0
    for item in t:
        if len(item) > item_size:
            item_size = len(item)
    return item_size       

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
        formated_data = str(character*(size-len(data)) + str(data))
        return str(formated_data)
    elif direction == 'right':
        formated_data = str(data) + str(character*(size-len(data)))
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

def list_function(t):
    while True:
        list_cmd = input("Enter a command(? for help): ")
        list_cmd = str(list_cmd.strip().lower())
        if list_cmd == '?':
            cmd_help()
        elif list_cmd == 'add':
            cmd_add(t)
        elif list_cmd == 'delete' or 'del':
            cmd_delete(t)
        elif list_cmd == 'list':
            cmd_list(t)
        elif list_cmd == 'clear':
            cmd_clear(t)
        elif list_cmd == '':
            print('exiting program')
            return quit()
        else:
            print('invalid command')

# Initialize list variable and run list function
default_list = []
list_function(default_list)

