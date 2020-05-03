# Assignment 3
# Marie Zazueta
# Write a program called “process_numbers.py” that repeatedly reads numbers input by the user
# until the user types “done”.
n = 0
while n > 0:
    line = input('Please enter a number or enter done when you are finished.')
    print (line)
    if line == 'done':
        print(line)

# After the user has entered “done”, print out (i.e. print) the total,
# count, maximum, minimum, and average of the entered numbers. Note that you are not
# allowed to use a list for this assignment. Lists are not covered until Chapter 8 of our textbook.
# total:
total = 0
for this_num in [n]:
 total += n
print('The total is ' + str(total))

# count:
count = 0
for this_num in [n]:
 count += 1
print('The number of items is ' + str(count))

# maximum:
maximum = None
for this_num in [n]:
 if maximum is None or this_num > maximum :
     maximum = this_num
print('The maximum value is ' + str(maximum))

# minimum:
minimum = None
for this_num in [n]:
 if minimum is None or this_num < minimum :
     minimum = this_num
print('The minimum value is ' + str(minimum))

# average:
average = None
for this_num in [n]:
 if average is None or this_num < average :
    average = this_num
print('The average number of items is ' +str(average))