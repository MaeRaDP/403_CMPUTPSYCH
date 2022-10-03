# Slicing exercises

# Create a list of numbers 0-100 called "list100"
list100 = list(range(0,101))
 
print(list100)
 
# Print first 10 numbers in list
print(list100[:10])
 
# Print all the odd numbers backwards
print(list100[99::-2])
 
# Print the last 4 numbers backwards
print(list100[100:96:-1])
 
# Are the 40th-44th numbers in the list equal to integers 39-43
list100 = list(range(0,101))
print(list100[39:44])
print(list(range(39,44)))

print(list100[39:44] == list(range(39,44)))
