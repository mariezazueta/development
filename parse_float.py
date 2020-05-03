# Assignment 3
# Marie Zazueta

# Given the following python statement…
# avg_str = 'Average value read: 0.72903'
# Use the find() method and string slicing to extract the portion of the string after the colon
# character
avg_str = 'Average value read: 0.72903'
avg_str.find(':')
print(avg_str[19:27])


# And then use the float() function to convert the extracted string into a floating
# point value.
f = float(avg_str[19:27])
print(f)