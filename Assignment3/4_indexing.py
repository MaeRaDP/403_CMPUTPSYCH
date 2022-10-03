# Indexing exercises

# Create a list of strings called "colors"
# red, orange, yellow, green, blue, purple

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# print penultimate color
print(colors[-2])

# print 3rd and 4th character of penultimate color
print(colors[-2][2] + colors[-2][3])

# remove purple, add indigo and violet to the list
colors.remove(colors[5])
colors.append('indigo')
colors.append('violet')
print(colors)