# CIS 122 Fall 2020 Assignment 8
# Author: Jacob Burke
# Partner: 
# Description: A program that allows a user to create their own groups that they
# would like to add data to. The groups themselves can also have assigned
# attributes  that the user can then assign data to. This is done through using
# a data structure that contains multiple layers of dictionaries and lists that
# interact with one another.

# Create functions:
def create_group(d):
    '''
    Creates a new group to add attributes to that can later be used by the user
    in creating dictionaries that have corresponding values to these attributes. 
    
    Extended Summary:
    Creates a new group to add attributes to that can later be used by the user
    in creating dictionaries that have corresponding values to these attributes.
    This is done through creating dictionaries within dictionaries. The first
    dictionary has the group name as the key, and the corresponding value is
    another dictinoary. This dictionary in itself is two dictionaries, one
    titled keys and another titled data. The keys dictionary will hold all the
    attributes that belong to the categories for the group. The data dictionary
    then holds a list of corresponding data dictionaries that relate back to the
    overall group.
    
    Args:
    d (dict): dictionary input

    Returns:
    None
    '''
    print("** Create new group**\n")
    while True:
        new_group = input("Enter group name (empty to cancel): ")
        new_group = str(new_group.strip())
        if new_group in d:
            print("Group already exists")
            return
        if new_group == '':
            break
        d[new_group] = {}
        if len(new_group) > 0:
            d[new_group] = {'_keys_': [], '_data_':[]}
            while True:
                properties = input( "Enter field name (empty to cancel): ")
                properties = str(properties.strip())
                if properties == '':
                    print('')
                    break
                d[new_group]['_keys_'].append(properties)


def list_group(d):
    '''
    Lists off groups that have already been created by the user.
    
    Extended Summary:
    Lists off groups that have already been created by the user. This is done
    with a for loop that will loop through and print out each corresponding
    group that exists.
    
    Args:
    d (dict): dictionary input

    Returns:
    None
    '''
    print(' **List of groups **')
    for i in sorted(d):
        print(str(i) + ' : ' + str(len(d[i]['_keys_'])) + ' properties (' + ', '.join(d[i]['_keys_']) + ') \n')


def add_group_data(d):
    '''
    Allows the user to add data to the group and corresponding attributes that
    they have created.
    
    Extended Summary:
    Allows the user to add data to the group and corresponding attributes that
    they have created. The function calls the list_group function to display
    groups that the user can add to. Then once a user types in a group from
    the prompt that displays, the function will loop through each corresponding
    attribute from the '_key_' dictionary that the user previously gave input
    values. 
    
    Args:
    d (dict): dictionary input

    Returns:
    None
    '''
    print("** Add group data **")
    list_group(d)
    while True:
        group = input("Enter group (empty to cancel): ")
        if group == '':
            break
        if group not in d:
            print("Group does not yet exist")
        elif d.get(group)['_keys_'] == []:
            print("Group has no attributes")
        else:
            dict_count = len(d.get(group)['_data_'])
            d.get(group)['_data_'].append({})
            for i in range(len(d.get(group)['_keys_'])):
                new_properties = input("Enter " + d.get(group)['_keys_'][i] + ": ")
                if new_properties == '':
                    break
                else:
                    d.get(group)['_data_'][dict_count][d[group]['_keys_'][i]] = new_properties
            if d.get(group)['_data_'][(dict_count)] == {}:
                del d.get(group)['_data_'][dict_count]


def list_group_data(d):
    '''
    Displays data for each corresponding group that the user selects.
    
    Extended Summary:
    Displays data for each corresponding group that the user selects. The
    function starts by calling the list_group function. Then it prompts the
    user to input the group they want data to be displayed from. Once a group
    is selected the function will loop through each corresponding dictionary
    item in the '_data_' key, and display each dictionary item as it's own
    sentence.
    
    Args:
    d (dict): dictionary input

    Returns:
    None
    '''
    print("** List group data **")
    list_group(d)
    while True:
        group = input("Enter group name (empty to cancel): ")
        if group == '':
            break
        if group not in d:
            print("Group does not yet exist")
        else:
            counter = 0
            for diction in d.get(group)['_data_']:
                sentence = ''
                for key in d.get(group)['_data_'][counter]:
                    sentence = sentence + ', ' + key + ' = ' + d.get(group)['_data_'][counter][key]
                sentence = sentence[2:]
                print(str(counter) + ' ' + sentence)
                counter = counter + 1

def cmd_help():
    '''
    Displays a list of available commands when called.
    
    Extended Summary:
    Displays a list of available commands when called.
    
    Args:
    None

    Returns:
    None    '''
    cmds = ['?', 'C', 'A', 'G', 'L', 'X']
    cmds_desc = ['list commands', 'Create a new group', 'Add data to a group', 'List groups', 'List data for a group', 'Exit']
    for i in range(len(cmds)):
        print(str(cmds[i]) + ': ' + str(cmds_desc[i]))
    print('Empty to exit')
    return

# Create group variable
#group = {}

def main_program():
    '''
    The main function that holds all related functions for the program. The user
    is prompted to enter commands, and can also display a list of available
    commands or exit the program. An error message will display if an invalid
    command is entered.
    
    Extended Summary:
    The main function that holds all related functions for the program. The user
    is prompted to enter commands, and can also display a list of available
    commands or exit the program. An error message will display if an invalid
    command is entered.
    
    Args:
    None

    Returns:
    None
    '''
    d = {}
    print(">> Welcome to Group Manager << \nThis program creates groups with dynamic properties")
    while True:
        main_cmd = input("\nCommand (empty or X to quit, ? for help: ")
        main_cmd = str(main_cmd.strip().upper())
        if main_cmd == '?':
            cmd_help()
        elif main_cmd == 'C':
            create_group(d)
        elif main_cmd == 'G':
            list_group(d)
        elif main_cmd == 'A':
            add_group_data(d)
        elif main_cmd == 'L':
            list_group_data(d)
        elif len(main_cmd) == 0 or main_cmd == 'X':
            print('exiting program')
            return quit()
        else:
            print('invalid command')
main_program()  
