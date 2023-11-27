# Function3.py
# @ author: Administrator
# Date: 31.10.23
 
first_number = 6
second_number = 4
 
def show_difference(number_1, number_2):
    print("The first number is {0}.\n"
          "The second number is {1}.\n"
          "The difference between them is {2}!!!\n"
          .format(number_1, number_2, number_1 - number_2)) # Minus number 2 from number 1
 
print("Welcome to my difference calculator...\n\n")
 
# invoking the function
show_difference(first_number, second_number)
 
# test case assertion
print("Test case assertion: if first number is 13 and second number is 2 "
    "then the difference should be 11!!")
show_difference(13, 2)
 
'''
Welcome to my difference calculator...
 
The first number is 6.
The second number is 4.
The difference between them is 2!!
'''

'''
If we break down this exercise, we start to get an idea of how the Abstract
Factory Method might work, as well as a glimpse at the Single Responsibility
Principle. The function is responsible for one calculation. The
show_difference is responsible for the calculation of the program. It has two
parameters, number_1 and number_2. If we were using the Abstract Factory
Method here, we would have the number variables as classes that would be
using the factory class of show_difference to instatiate the numbers as
objects. Then we could do the calculation in the main method to receive the
results.
'''
