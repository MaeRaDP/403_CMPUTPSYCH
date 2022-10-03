# PSYCH 403 - Assignment 4 exercises: MPacificar

## Conditional exercises
1. You want to tell your experiment to record participant responses. If the response is "1" or "2", print OK. If the response is "NaN" (empty), print a "subject did not respond" message. If the response is anything else, print "subject pressed the wrong key".
```
response = '1'

if response == '1' or response == '2':
    print("OK")
elif response == 'NaN':
    print("subject did not respond")
else: print("subject pressed the wrong key")
```
2. Create a nested "if" statement in the above exercise. If the response is "1", print "Correct!". If the response is "2", print "Incorrect!"
```
response = '1'

if response == '1' or response == '2':
    print("OK")
    if response == '1':
        print("Correct!")
    if response == '2':
        print("Incorrect!")
elif response == 'NaN':
    print("subject did not respond")
else: print("subject pressed the wrong key")
```
3. Test out your script with various responses. Does it do what you expect it to?
- **Answer:** I tested out my script with response = '1', response = '2', response = 'NaN', response = '' and it does what I expect it to do.

## For loop exercises
Remember the exercise where you printed each letter of your name? 
1. Create a for loop that prints each letter without writing out all of the print statements manually.
```
my_name = 'MAE'

for each_letter in my_name:
    print(each_letter)
```
2. Add an index counter and modify your loop to print the index number after each letter
```
my_name = 'MAE'
counter = -1

for each_letter in my_name:
    counter = counter+1
    print(each_letter)
    print("This letter has an index of %i" %counter)
```
3. Create a list of names "Amy","Rory", and "River". Create a nested for loop to loop through each letter of each name.
```
name_list = ['Amy','Rory','River']

for names in name_list:
    print(names)
    for each_letter in names:
        print(each_letter)
```
4. Add an index counter that gives the index of each letter for each name. The counter should start over at 0 for each name in the list.
```
name_list = ['Amy','Rory','River']

for names in name_list:
    print(names)
    counter = -1
    for each_letter in names:
        counter = counter+1
        print(each_letter)
        print("This letter has an index of %i" %counter)
```

## While loop exercises
1. Create a while loop of 20 iterations that prints "image1.png" for the first 10 iterations, and "image2.png" for the next 10 iterations.
```
```
2. Create a while loop that shows an image until the participant makes a response of 1 or 2. Run it a few times to make sure it works the way you expect.
```
```
3. Create a failsafe that terminates the previous while loop after 5 iterations if one of the valid responses (1,2) have not been made in that time.
```
```
