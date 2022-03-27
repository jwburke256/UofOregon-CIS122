# CIS 122 Fall 2020 Lab 10
# Author: Jacob Burke
# Partner: 
# Description:

def number_stats(*args):
    total = 0
    count = len(args)
    min_value = -1
    max_value = 0
    mean = 0
    median = 0
    for num in args:
        total += num
        if num > max_value:
            max_value = num
        if min_value == -1 or num < min_value:
            min_value = num

        if len(args) > 0:
            mean = total / len(args)

        t = sorted(args)

        if len(t) == 1:
            median = args[0]
        elif len(t) % 2 == 0:
            pos1 = (len(t) // 2)
            pos2 = (len(t) // 2) -1
            median = (t[pos1] + t[pos2]) / 2
        else:
            median = t[len(t) // 2]
            
    return count, min_value, max_value, mean, median


numbers = (10, 20, 30, 40)
count, min_value, max_value, mean, median = number_stats(*numbers)
print('Count: ' + str(count) + '\nMin: ' + str(min_value) + '\nMax: ' + str(max_value) + '\nMean: ' + str(mean) + '\nMedian: ' +str(median))
