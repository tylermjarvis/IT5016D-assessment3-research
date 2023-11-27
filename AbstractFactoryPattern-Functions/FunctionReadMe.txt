# Folder Title
AbstractFactoryPattern-Functions


# Folder Description
This folder delves into the abstract factory pattern with methods, which are similar to functions, as well as my learning journey with functions. Functions can 
be used to return data or supply the program with a task that executes a behaviour based on the code block. Functions can be used in various Python design 
patterns, due to them acting in a similar fashion to methods (methods are within classes).
There is a difference between functions in the fact that they can be called from anywhere, where as methods are tied to class objects. Because they are similar 
to methods, they can be used in a similar way when approaching Python design patterns. I have chosen the abstract factory method to showcase how you would use 
a function or method to break down the problem of displaying a list of courses, without having to manually instantiate them.

There is a folder with the answers to Learning Activities 46, 47 and 49. These answers have helped me conceptualise how functions are used and how to call them
appropriately. They have also taught me about functions that return a value and functions with parameters.

There is also a folder with all my practice code, carried out during the learning activities, which include comments and brief descriptions (some exercises) 
of why functions are used. The comments break down the problems so that they are easy to follow, as well as apply ideas on how the Abstract Factory Method may be 
used with these problems and with Python functions.

There is one Python file (AbstractFactoryMethod.py) that takes a Python Design Pattern example from GeeksforGeeks and applies it to how a specific Python syntax 
may be used with this pattern. I also analyses this example, by breaking it down and explaining the scenario/problem that the pattern is solving, to get a better 
understanding of this particular Python Design Pattern. I then study how this pattern and the learning examples work towards following the Python design principles.
For example:
Functions with the Abstract Factory Method pattern cater to the Single Responsibility Principle.


# More Information
Please look at the Python files and screenshots for more specific comments relating to each exercise and how specific examples relate to Python 
design principles and patterns.


# How Functions Work
def show_my_message():
    print("Hello!")

# To call the function
show_my_message()


# Context of Design Pattern
The Abstract Factory Method Pattern is a creational design pattern that allows us to solve the problem of creating different products without using instantiating
classes. Therefore the actual products are created using the factory class.

An advantage of the Abstract Factory Method Pattern is that we can introduce new variants of a product without changing the base code. We also receive products
that are compatible with each other, due to the factory class creating them together.


# Python Design Patterns
Abstract Factory Method Pattern - allows us to create products without using instantiating classes. The factory class deals with this behaviour.