# Folder Title
ExceptionHandlingPattern-Debugging


# Folder Description
This folder analyses Debugging in PyCharm (IDE) and the Exception Handling Pattern. This allows us to catch errors in the code, before we let other code blocks run. 
This helps with unit testing, debugging and flow control. We are given numerous error exceptions in Python that explain to us how the code is working and what it is 
expecting as an input, as well as what the program is outputting. There are coding examples within this file that introduce some of these error exceptions and how they 
help us produce clean and concise code that informs the user and the program of every possible result.

There is a folder called pythonProject which holds the PyCharm code examples. It includes answers and my own code which has helped me conceptualise how debugging works
in an IDE.


# More Information
Please look at the following Python code files for more specific comments relating to each exercise and how specific examples relate to Python 
design principles and patterns.


# How Debuggin Works
When using IDE's such as PyCharm, we have access to a debugging function that allows us to select a point in our
program and run the code to that point to see the behaviour and the variables that are being returned. We can also
skip over code lines or step in and out of functions that are being called.


# Context of Design Pattern
To use the Exception Handling Pattern, we need to supply the try, except, else, finally statement or another conditional statement with a known exception error provided by Python.
This will instruct the program on what error to expect and what message to send the program if that error is encountered. It is important that you know what errors are being
registered within the program so that there are no surprises when it comes to debugging and testing.

An advantage of the Exception Handling Pattern is that it allows us to deal with errors in an appropriate way, making our code more reliable and efficient.


# Python Design Patterns
Exception Handling Pattern - allows us to deal with errors throughout our program, and therefore test and debug more appropriately.