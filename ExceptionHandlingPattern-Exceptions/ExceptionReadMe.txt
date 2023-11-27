# Folder Title
ExceptionHandlingPattern-Exceptions


# Folder Description
This folder delves into exceptions and the Exception Handling Pattern that allows us to catch errors in the code, before we let other code blocks run. This helps with unit testing, debugging and flow control.
We are given numerous error exceptions in Python that explain to us how the code is working and what it is expecting as an input, as well as what the program is outputting.
There are coding examples within this file that introduce some of these error exceptions and how they help us produce clean and concise code that informs the user and the program of every possible result.

There is a folder with the answers to Learning Activity 53. These answers have helped me conceptualise how exceptions work and the try, except, else, finally process.

There is also a folder with all my practice code, carried out during the learning activities, which include comments and brief descriptions of why exceptions are
used. The comments break down the problems so that they are easy to follow, as well as apply ideas on how the Exception Error Handling pattern may be used with these problems.

There is one Python file (ExceptionHandlingPattern.py) that takes a Python Design Pattern example and applies it to how Python exceptions may be used with this pattern.
I also analyses this example, by breaking it down and explaining the scenario/problem that the pattern is solving, to get a better understanding of this particular 
Python Design Pattern. I then study how this pattern and the learning examples work towards following the Python design principles.


# More Information
Please look at the following Python code files and screenshots for more specific comments relating to each exercise and how specific examples relate to Python 
design principles and patterns.


# How Error Exceptions Work
def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Error, cannot divide by zero!"
 
print(divide_numbers(3,0))
 
Output
Error, cannot divide by zero!


# Context of Design Pattern
To use the Exception Handling Pattern, we need to supply the try, except, else, finally statement or another conditional statement with a known exception error provided by Python.
This will instruct the program on what error to expect and what message to send the program if that error is encountered. It is important that you know what errors are being
registered within the program so that there are no surprises when it comes to debugging and testing.

An advantage of the Exception Handling Pattern is that they allow us to deal with errors in an appropriate way, making our code more reliable and efficient.


# Python Design Patterns
Exception Handling Pattern - allows us to deal with errors throughout our program, and therefore test more appropriately.