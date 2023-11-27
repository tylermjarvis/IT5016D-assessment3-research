# Folder Title
DecoratorPattern-Booleans


# Folder Description
This folder contains all of my practice with the boolean data type. Most of my practice at the begining is to do with the Learning Activities for the boolean logic in 
Module 2: Part 4. It also includes the files with the answers to these activites (In Boolean Answers), as the answers have assisted my learning journey with booleans and 
how to process the conditional logic. The learning curb with booleans, is that they are the thought process behind the planning stage of a program. You often break a problem 
up into different available options, which is what a boolean leads to. Conditional statements use boolean operations, such as and, or, > and <. They help a programmer break 
a problem into everyday situations, where we often make decisions which affect an outcome. 
Each Learning Exercise starts with the more basic concepts of a boolean, such as variable = True or this_variable = False.
Then conditional statements are introduced which assist more complex problems. For example, asking the user if they would like to calculate the area or volume of a shape or 
is the magnitude of an earthquake going to respond to the user with a dangerous earthquake or not dangerous earthquake.
The files within this folder also include !=, == and not as a way to check if the conditional is equal or not equal to another value.
My understanding with boolean logic is that it is often used in coding programs to decide what choice or code block the program should execute based on a True vs False rule.

There is a folder with the answers to all the boolean Learning Activities 31, 33, 34 and 35. These answers have assisted my learning of booleans.

There is also a folder with all my practice code, carried out during the learning activities, which include comments and brief descriptions (some exercises) of why booleans are
used. The comments break down the problems so that they are easy to follow, as well as apply ideas on how the Decorator Method may be used with these problems.

There is one Python file (DecoratorMethodExample.py) that takes a Python Design Pattern example from GeeksforGeeks and applies it to how a specific Python syntax may be used with this pattern.
I also analyses this example, by breaking it down and explaining the scenario/problem that the pattern is solving, to get a better understanding of this particular 
Python Design Pattern. I then study how this pattern and the learning examples work towards following the Python design principles.
For example:
Using boolean operations with the Decorator Method pattern which cater to the Single Responsibility Principle.


# More Information
Please look at the following Learning Activity Python files for more specific comments relating to each exercise and how specific examples relate to Python design principles 
and patterns.


# To Note
The conditional if statement order is important, due to options being missed if they are True for multiple cases. For example:
if i % 5 == 0 and i % 3 == 0: # This condition needs to come first otherwise i will print "Buzz" instead of "FizzBuzz"
	print(“FizzBuzz”)
elif i % 3 == 0:
	print(“Fizz”)
elif i % 5 ==0:
	print(“Buzz”)
else:
	print(i)


# How a Conditional Statements Work
if (True condition is met):
	Do code...
elif (Another statement is true):
	Do this code...
else:
	Nothing was True so do this code...


# Context of Design Patterns
If Statements (Conditional Statements) can be used towards a variety of design patterns, due to their ability to dynamically shift data/code based on the conditions that 
are presented to them.
Some examples of design patterns that they can be used with are:
The Decorator Pattern - Conditional statements can add behaviour to objects based on new conditions to modify the outcome of an object.
The Mediator Pattern - Because conditional statements change the behaviour of a program, they offer as a mediator, shaping the direction that the program will run.

As seen above, conditional statements mainly have an affect on behavioural patterns, due to their nature of changing the programs outcome at run time.


# Python Design Patterns Studied
The Decorator Pattern - Uses decorator functions to wrap new behaviours over an object.