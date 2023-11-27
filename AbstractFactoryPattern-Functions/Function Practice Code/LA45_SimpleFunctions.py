# LA45_SimpleFunctions.py
# @ author: Administrator
# Date: 30.10.23

import random

# Task 1 - add the sum of numbers
def add_numbers():
    print("Welcome to the interger displayer!!! Here is the sum of two intergers:")
    sum = 5 + 8
    print(sum, "\n")
    
print("Testing user defined functions...\n\n")
 
# invoking Task 1 function
add_numbers()
 
# Task 2 - print a string 5 times
def print_y():
    print("The is task 2:")
    x = 5
    y = "A string\n"
    print(y * 5)

# invoking Task 2 function
print_y()

# Task 3 - display a random number in range of 1 to 100 while user keeps typing r
def random_number():
     user_input = input("Please type r to select a random number:")
     while user_input == "r":
         print(random.randint(1, 100))
         user_input = input("Please type r to select a random number:")
     else:
         return

# invoking Task 3 function
random_number()
 
'''
Outputs
Testing user defined functions...


Welcome to the interger displayer!!! Here is the sum of two intergers:
13 

The is task 2:
A string
A string
A string
A string
A string

input = r
Please type r to select a random number:r
4

input = r
Please type r to select a random number:r
24

input = r
Please type r to select a random number:r
55

input = r
Please type r to select a random number:r
56

input = y
Please type r to select a random number:y
'''

'''
These examples above show the complexity that functions can have. They can be
as simple as adding numbers and printing strings or using user input to
loop through random numbers. This gives us an idea of how we can use functions
for a variety of problems.
'''
