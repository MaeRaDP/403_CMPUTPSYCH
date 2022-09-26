# My answers to Assignment 2 exercise questions:

## **Print exercises:**
```
print('M')
print('A')
print('E')
```
- Question: Do any variables show up in the Variable Editor (for yourname.py)?
  - Answer: No - no variables show up in Spyder's Variable Explorer when I run the script that prints my first name, one letter at a time.


## **Operation exercises:**
```
print(5 / 2) 
print(5.0 / 2.0) 
```
- Question 1: Does Python output the same values for these? If you got a different answer for the two operations, explain why.
  - Answer: Yes - Python output the same values when you do these operations.
```
print(90 % 4) 
```
- Question 2: What does the modulo operator (%) do?
  - Answer: The modulo operator output the remainder when dividing two integers. (E.g., it output 2 for 90 % 4)
```
print(10 ** 3) 
print(15 // 6) 
```
- Question 3: What do these operators do: ** and //?
  - Answers: 
  - ** operator - raises number on the left of ** to the power of the number on the left of **. (E.g., 10 ** 3 output 1000)
  - // operator - divides the number on the left of // with the number on the right and output the smallest integer. (E.g., 15 // 6 output 2)
```
print(1 + 6 + 8 * 9 / 3) 
```
- Question 4: Does Python follow order of operations?
  - Answer: Yes - Python follows order of operations. (E.g., 1 + 6 + 8 * 9 / 3 output 31.0)

## **Variable exercises:**
```
# First name's variables: Each letter of the name as separate variable
letter1 = ('M')
letter2 = ('A')
letter3 = ('E')
```
- Question 1: Do any variables show up in the Variable Editor?
  - Answer: Yes - letter1, letter2, and letter3 all show up in the Variable Explorer as strings (type) along with their given values.
```
# First name's variables, letterX same as letter1:
letter1 = ('M')
letter2 = ('A')
letter3 = ('E')
letterX = ('M')
# Print letterX and letter1 on the same command line
print(letter1+letterX)
```
- Question 2: Does Python have a problem with two different variables having the same value?
  - Answer: No - Python does not have a problem with two different variables with the same value. (E.g., letter1 and letterX having the value of 'M')
```
# First name's variables, letterX is given a new letter:
letter1 = ('M')
letter2 = ('A')
letter3 = ('E')
letterX = ('X')
# Print letterX and letter1
print(letter1)
print(letterX)
```
- Question 3: Did changing the value of letterX change the value of the other variable(s)?
  - Answer: No - changing letterX's value doesn't change letter1's value.
```
# First name's variables, letterX=letter1:
letter1 = ('M')
letter2 = ('A')
letter3 = ('E')
letterX = letter1
# Print letterX and letter1
print(letter1)
print(letterX)
        
# First name's variables, letterX=letter1, letter1 is 'z':
letter1 = ('z')
letter2 = ('A')
letter3 = ('E')
letterX = letter1
# Print letterX and letter1
print(letter1)
print(letterX)
```
- Question 4: Did changing the value of letter1 change the value of letterX? What does this tell you about python variable assignment?
  - Answer: Yes - changing the value of letter1 changed the value of letterX, when letterX=letter1. When you create a variable, Python assigns the value of that variable with what is given to the right of the equal sign. We can also assign a different variable to equate a pre-existing variable (E.g., letterX=letter1). We can reassign different values to variables without impacting/changing existing variables (E.g., change value of letterX without changing letter1). 
  
## **Boolean exercises:**
```
# Are 1 and 1.0 equivalent?
print(1 == 1.0)
# Are "1" and "1.0" equivalent?
print('1' == '1.0')
```
- Question 1: Are 1 and 1.0 equivalent? Are "1" and "1.0" equivalent? Why do you think this is?
  - Answers: 
  - Yes - 1 and 1.0 are equavalent to each other because they are the same number Python output True given 1 == 1.0.
  - No - "1" and "1.0" are not equivalent because they are not integers or floats, they are types of strings in Python. To be equivalent, the text within the " " should be the exactly the same.
```
# Are 5 and (3+2) equivalent?
print(5 == (3+2))
```
- Question 2:
  - Answer: Yes - 5 and (3+2) are equivalent because they mean the same thing mathematically.
- Question 3: List 5 ways to get True as your output for the given statements:
  - Answer:
```
# [Are 1 and 1.0 equivalent?] X [Are "1" and "1.0" equivalent?] X [Are 5 and (3+2) equivalent?]
# 5 ways to get True as output
print(1 == 1.0 and not '1' == '1.0' and 5 == (3+2)) #True
print(1 == 1.0 and not '1' == '1.0' or 5 == (3+2)) #True
print(1 == 1.0 and '1' == '1.0' or 5 == (3+2)) #True
print(1 == 1.0 or'1' == '1.0' or 5 == (3+2)) #True
print(1 == 1.0 or '1' == '1.0' and 5 == (3+2)) #True
```


## **List exercises:**
```
# create oddlist - odd integers between 0 and 10
oddlist = [1,3,5,7,9]
print(oddlist)
```
- Question 1: Did oddlist become a variable?
  - Answer: Yes - oddlist became a variable.
```
# use len fn on oddlist
print(len(oddlist))
```
- Question 2: When you use the "len" function on oddlist, how long does python say the list is?
  - Answer: Python says the length of the list is 5.
```
# use type fn on oddlist
print(type(oddlist))
```
- Question 3: When you use the "type" function on oddlist, what type of variable does python say oddlist is?
  - Answer: Python says the variable oddlist is a type of list.
```
# create intlist - listing all integers between 0 and 100
intlist = list(range(1,100))
print(intlist)
```
- Question 4: Print intlist. Does it list all integers between 0 and 100?
  - Answer: Yes - intlist prints all integers between 0 and 100.

## **Dictionary exercises:**
```
# about_me variables:
my_name = 'Mae' #string
my_age = 27.0 #float
my_study_year = 4 #integer
my_fave_foods = ['sashimi','sushi','ramen','korean bbq','seafood','pho','karekare','lechon','dessert'] #list

# create an about_me dictionary:
about_me = {
    'name':my_name,
    'age':my_age,
    'yearstudy':my_study_year,
    'favefoods':my_fave_foods
    }
print(about_me)
print(type(about_me))
print(len(about_me))
```
- about_me type confirms that I have made a dictionary.
- Question: How does python determine the length of a dictionary?
  - Answer: The length of about_me dictionary is 4. Python determines the length of a dictionary by counting the number of objects (e.g., the variables separated by comma ,) stored in the dictionary.

## **Array exercises:**
```
import numpy as np
```
```
# Array called "mixnums" composed of 3 integers and 3 floats. Then print.
mixnums = np.array([9, 4, 13, 17.5, 14.1, 21.2])
print(mixnums)
```
- Question 1: Create an array called "mixnums" composed of 3 integers and 3 floats. Print the array. What has happened to the array?
  - Answer: Python output of the mixnums array shows all the integers converted into floats.
```
# Create an array called "mixtypes" composed of 2 integers, 2 floats, and 2 strings. Then print.
mixtypes = np.array([12, 6, 21.5, 12.7, 'circe', 'helios'])
print(mixtypes)
```
- Question 2: Create an array called "mixtypes" composed of 2 integers, 2 floats, and 2 strings. Print the array. What has happened to the array? What does python do to arrays with mixed types?
  - Answer: Python output of mixtypes array shows all the integers and floats converted into strings.
```
# Create an array called "oddarray" of all odd numbers between 0 and 100. Then print.
oddarray = np.arange(1,100,2)
print(oddarray)
```
```
# Create an array called "logarray" of 16 numbers between 1 and 5 that follow a logarithmic distribution. Then print.
logarray = np.logspace(1,5,16)
print(logarray)
```
