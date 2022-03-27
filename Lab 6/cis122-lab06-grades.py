# CIS 122 Fall 2020 Lab 6
# Author: Jacob Burke
# Partner: 
# Description: User can input grades into the program. Once all grades have been
# entered, the user can just hit enter. This will cause the program to finish
# and the results to be displayed, which include total count of grades put in,
# average grade, lowest grade, and the highest grade.

#Initialize variables
input_grades = True
total_score = 0
total_count = 0
average_score = 0
low_score = -1
high_score = -1

# Input grades
while input_grades == True:
    input_score = input('Enter score: ')
    input_score
# Exit the game if no score input
    if (len(input_score)) == 0:
        print("No scores entered")
        input_grades = False
    else:
        input_score = int(input_score)
        if input_score == 0:
            total_score = total_score + input_score
            total_count = total_count + 1
        else:
            total_score = total_score + input_score
            total_count = total_count + 1
            average_score = total_score / total_count
            if low_score == -1:
                low_score = input_score
            else:
                if input_score < low_score:
                    low_score = input_score
                else:
                    pass
            if high_score == -1:
                high_score = input_score
            else:
                if input_score > high_score:
                    high_score = input_score
                else:
                    pass
        

# Once loop ends print the results
print('*** Results ***')
print('Count: \t' + str(total_count))
print('Average: \t' + str(average_score))
print('Low score: \t' + str(low_score))
print('High score: \t' + str(high_score))
