# For loop exercises

# 1. Remember the exercise where you printed each letter of your name? 
# Create a for loop that prints each letter without writing out all of the print statements manually.
my_name = 'MAE'

for each_letter in my_name:
    print(each_letter)
    
    
# 2. Add an index counter and modify your loop to print the index number after each letter
my_name = 'MAE'
counter = -1

for each_letter in my_name:
    counter = counter + 1
    print(each_letter)
    print("This letter has an index of %i" %counter)

# 3. Create a list of names "Amy","Rory", and "River". 
# Create a nested for loop to loop through each letter of each name.

name_list = ['Amy','Rory','River']

for names in name_list:
    print(names)
    for each_letter in names:
        print(each_letter)


# 4. Add an index counter that gives the index of each letter for each name. 
# The counter should start over at 0 for each name in the list.

name_list = ['Amy','Rory','River']

for names in name_list:
    print(names)
    counter = -1
    for each_letter in names:
        counter = counter + 1 
        print(each_letter)
        print("This letter has an index of %i" %counter)