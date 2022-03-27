# CIS 122 Fall 2020 Assignment 5
# Author: Jacob Burke
# Partner: 
# Description: A simple guessing game that prompts the user for the word to be
# guessed, then prompts for a guess of a letter in the word. Once all letters
# have been found, the game ends and the results are displayed.

# Defining functions to be used in guessing game:
def verify_emptiness(string):
    '''
    Verifies if a user input was empty, and if so exits the game.

    Extended Summary:
    Verifies if a user input was empty through a conditional , and if so exits
    the game.

    Args:
    string (str): string input

    Returns:
    Exits the game or returns none
    '''
    if (len(string)) == 0:
        print('exiting')
        quit()
    else:
        return

def check_string(guess_word):
    '''
    Takes a string and calculates the amount of unique characters in the string,
    and outputs that amount as an integer.

    Extended Summary:
    Takes a string and calculates the amount of unique characters in the string.
    This is done through an if loop, where it checks each character and if the
    character hasn't been seen before, it adds it to a temporary variable. The
    function then outputs the temporary variables final amount as an integer.

    Args:
    guess_word (str): string input

    Returns:
    Returns the amount of unique characters in the string as an integer
    '''
    unique_string = ''
    for character in guess_word:
        if character not in unique_string:
            unique_string = unique_string + character
    return unique_string

def guessing_game(guess_word):
    '''
    Takaes a guess word and runs a guessing game. The user inputs a letter they
    think is in the word. The game then prints if the letter is in the word or
    not, and displays the guesses so far. Once all letters in the word have been
    guessed, the game ends and the final results are displayed.

    Extended Summary:
    Takaes a guess word and runs a guessing game. The game runs until complete
    using a while loop, until all letters have been guessed. The user is
    prompted to input a letter they think is in the word. The game then checks
    the letter. If no letter is inputed the game exits. If the user inputs
    multiple letters then the game prints an error message and reprompts the
    user. If the letter is found, already found, not found, or already not found
    the game displays the message respectively and also shows the total guesses
    displayed below. Once all letters in the word have been guessed, the game
    ends and the final results are displayed. Results displayed are the word,
    letters matched in word, letters guessed but not in the word, and the total
    number of guesses till all letters were found.

    Args:
    guess_word (str): string input

    Returns:
    None
    '''
    guess_counter = ''
    wrong_guess_counter = ''
    total_guess_counter = 0
    while len(guess_counter) != len(unique_string):
        # Prompt the user for a letter
        guess_letter = input('Enter a guess letter (blank to quit): ')
        guess_letter
        verify_emptiness(guess_letter)
        if len(guess_letter) > 1:
            print('\t > Only enter a single letter')
        elif (guess_letter in wrong_guess_counter) == True:
            total_guess_counter = total_guess_counter + 1
            print('\t > ' + str(guess_letter) + ' already guessed and not found')
            print('\t > Guesses so far: ' + str(guess_counter) + str(wrong_guess_counter))
        elif (guess_letter in guess_counter) == True:
            total_guess_counter = total_guess_counter + 1
            print('\t > ' + str(guess_letter) + ' already guessed and found')
            print('\t > Guesses so far: ' + str(guess_counter) + str(wrong_guess_counter))
        elif (guess_letter in guess_word) == True:
            total_guess_counter = total_guess_counter + 1
            guess_counter = guess_counter + str(guess_letter)
            print('\t > ' + str(guess_letter) + ' found')
            print('\t > Guesses so far: ' + str(guess_counter) + str(wrong_guess_counter))
        else:
            total_guess_counter = total_guess_counter + 1
            wrong_guess_counter = str(guess_letter) + wrong_guess_counter
            print('\t > ' + str(guess_letter) + ' not found')
            print('\t > Guesses so far: ' + str(guess_counter) + str(wrong_guess_counter))
    print('\t > All letters found')
    print('\n*** Results ***')
    print('Word: \t \t' + str(guess_word))
    print('Matched: \t' + str(guess_counter))
    print('Unmatched: \t' + str(wrong_guess_counter))
    print('Guesses: \t' + str(total_guess_counter))

# Prompt the user for a guess word
guess_word = input('Enter a guess word (blank to quit): ')
guess_word
length_of_word = len(guess_word)

# Empty word will exit the program
verify_emptiness(guess_word)

# Create function that pulls unique characters out of a string and makes it a
# string
unique_string = check_string(guess_word)

# The guessing game starts once the guess_word has been input
guessing_game(guess_word)
