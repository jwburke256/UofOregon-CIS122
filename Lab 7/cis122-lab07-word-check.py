# CIS 122 Fall 2020 Lab 7 Part 1
# Author: Jacob Burke
# Partner: 
# Description: Prompts the user for a word, and then checks a text file to
# determine if the word is found in the file. The program then prints the
# results for the user.

# Assign Variables:
text_file = "words_alpha.txt"

# Create Functions
def find_word_in_file(text_file, target_word):
    '''
    Opens the file inputed as a parameter of the function. The fuction then
    loops through each line of the file looking for the target word used as the
    parameter. If the word is found, the file is closed and function returns
    True. If it isn't found, the loop ends and the function returns False.
    
    Extended Summary:
    Opens the file inputed as a parameter of the function. The fuction then
    loops through each line of the file looking for the target word used as the
    parameter. If the word is found, the file is closed and function returns
    True. If it isn't found, the loop ends and the function returns False.
    
    Args:
    text_file (str): file input
    target_word (str): word to be searched

    Returns:
    Either True if word found or False if word not found
    '''
    fin = open(text_file)
    line_count = 0
    for line in fin:
#        line_count = line_count + 1
        if line.strip() == target_word:
            print(line_count)
            # Close file
            fin.close()
            return True
    # Close file
    fin.close()
    # Print results
#    print(str(line_count))
    return False


# While loop to prompt user for a word to search, if no word is input then the
# loop will end.
while True:
    word = input('Enter a search word (blank to exit): ')
    word = word.strip() #Removes leading and trailing whitespace
    # used to match the word as if it were lower case
    lower_word = word.lower()
    if len(word) == 0:
        # Exit if nothing entered
        break
    # Perform search and Print Results
    if find_word_in_file(text_file, lower_word) == True:
        print("Word " + str(word) + " found")
    else:
        print("Word " + str(word) + " not found")
    


