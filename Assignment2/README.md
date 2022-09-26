# My answers to Assignment 2 exercise questions:

## **Print exercises:**
- Question: Do any variables show up in the Variable Editor (for yourname.py)?
  - Answer: No - no variables show up in Spyder's Variable Explorer when I run the script that prints my first name, one letter at a time.


## **Operation exercises:**
- Question 1: Divide 5/2 (integer format) and 5.0/2.0 (float format). Does Python output the same values for these? If you got a different answer for the two operations, explain why.
  - Answer: Yes - Python output the same values when you do these operations 5/2 and 5.0/2.0.
- Question 2: What does the modulo operator (%) do?
  - Answer: The modulo operator output the remainder when dividing two integers. (E.g., it output 2 for 90 % 4)
- Question 3: What do these operators do: ** and //?
  - Answer: 
  - ** operator - it raises number on the left of ** to the power of the number on the left of **. (E.g., 10 ** 3 output 1000)
  - // operator - divides the number on the left of // with the number on the right and output the smallest integer. (E.g., 15 // 6 output 2)
- Question 4: Does Python follow order of operations?
  - Answer: Yes - Python follows order of operations. (E.g., 1 + 6 + 8 * 9 / 3 output 31.0)

## **Variable exercises:**
- Question 1: Do any variables show up in the Variable Editor?
  - Answer: Yes - letter1, letter2, and letter3 all show up in the Variable Explorer as strings (type) along with their given values.
- Question 2: Does Python have a problem with two different variables having the same value?
  - Answer: No - Python does not have a problem with two different variables with the same value. (E.g., letter1 and letterX having the value of 'M')
- Question 3: Did changing the value of letterX change the value of the other variable(s)?
  - Answer: No - changing letterX's value doesn't change letter1's value.
- Question 4: Did changing the value of letter1 change the value of letterX? What does this tell you about python variable assignment?
  - Answer: Yes - changing the value of letter1 changed the value of letterX, when letterX=letter1. When you create a variable, Python assigns the value of that variable with what is given to the right of the equal sign. We can reassign different values to variables without impacting/changing existing variables.
  
## **Boolean exercises:**
- Question 1: Are 1 and 1.0 equivalent? Are "1" and "1.0" equivalent? Why do you think this is?
  - Answer: Yes - 1 and 1.0 are equavalent to each other because they are the same number. Python output True given 1 == 1.0.
- Question 2:
  - Answer: Yes - 5 and (3+2) are equivalent because they mean the same thing mathematically.
- Question 3: List 5 ways to get True as your output for the given statements:
  - Answer:
  - 1. (1 == 1.0 and not '1' == '1.0' and 5 == (3+2))
  - 2. (1 == 1.0 and not '1' == '1.0' or 5 == (3+2))
  - 3. (1 == 1.0 and '1' == '1.0' or 5 == (3+2))
  - 4. (1 == 1.0 or'1' == '1.0' or 5 == (3+2))
  - 5. (1 == 1.0 or '1' == '1.0' and 5 == (3+2))

## **List exercises:**
- Question 1: Create a list called "oddlist", listing all of the odd integers between 0 and 10. Did oddlist become a variable?
  - Answer: Yes - oddlist became a variable
- Question 2: When you use the "len" function on oddlist, how long does python say the list is?
  - Answer: Python says the length of the list is 5.
- Question 3: When you use the "type" function on oddlist, what type of variable does python say oddlist is?
  - Answer: Python says the variable oddlist is a type of list
- Question 4: Print intlist. Does it list all integers between 0 and 100?
  - Answer: Yes - intlist prints all integers between 0 and 100.

## **Dictionary exercises:**
- Question: How does python determine the length of a dictionary?
  - Answer: The length of about_me dictionary is 4. Python determines the length of a dictionary by counting the number of variables stored in the dictionary.

## **Array exercises:**
- Question 1: Create an array called "mixnums" composed of 3 integers and 3 floats. Print the array. What has happened to the array?
  - Answer: Python output of the mixnums array shows all the integers converted into floats.
- Question 2: Create an array called "mixtypes" composed of 2 integers, 2 floats, and 2 strings. Print the array. What has happened to the array? What does python do to arrays with mixed types?
  - Answer: Python output of mixtypes array shows all the integers and floats converted into strings.
