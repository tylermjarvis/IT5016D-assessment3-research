# Folder Title
MediatorPattern-Strings


# Folder Description
This folder delves into Python Strings and using them within the State Method Pattern. Strings can be used within a variety of Python design patterns, but I have
chosen the Mediator Method to showcase how they can be used to create tidier and more efficient code. Strings are a combination of characters that hold a value
based on the characters themselves. The computer is unaware that they are actual words as it stores them as bytes. There are numerous exercises within this folder that have
helped me become familiar with strings and how to use them in a way that solves complicated problems and abides by design principles.

There is a folder with the answers to Learning Activities 50, 51, and 52. These answers have helped me conceptualise how strings can be used for processes, such as being 
a value, being used within conditional statements and used within classes.

There is also a folder with all my practice code, carried out during the learning activities, which include comments and brief descriptions (some exercises) of why strings are
used. The comments break down the problems so that they are easy to follow, as well as apply ideas on how the Mediator Method may be used with these problems.

There is one Python file (MediatorMethodExample.py) that takes a Python Design Pattern example from GeeksforGeeks and applies it to how a specific Python syntax may be used with this pattern.
I also analyses this example, by breaking it down and explaining the scenario/problem that the pattern is solving, to get a better understanding of this particular 
Python Design Pattern. I then study how this pattern and the learning examples work towards following the Python design principles.
For example:
Using string methods with the Mediator Method pattern which cater to the Inheritance and Single Responsibility Principles.


# More Information
Please look at the following Python code files and screenshots for more specific comments relating to each exercise and how specific examples relate to Python 
design principles and patterns.


# How Lists Work
string_1 = "Hello World"
 
print("Using the join method to add a whitespace between every char...\n{0}"
      .format(" ".join(string_1)),

# Output
H e l l o   W o r l d


# Context of Design Pattern
The Mediator Method Pattern is a behavioural design pattern that allows us to reduce the dependencies between objects. We use the mediator class so
that the objects can communicate with each other. This reduces coupling, as we only have one dependency involved in the communication.
It works in the same way a router would connect different devices. The router moves the data to where it needs to be.

An advantage of the Mediator Method Pattern is that we have classes that are responsible for their content and data and the mediator class,
which is responsible for the communication between objects. Therefore we are abiding by the Single Responsibility Principle.


# Python Design Patterns Studied
Mediator Method Pattern - allows us to use a mediator to communicate between different objects.