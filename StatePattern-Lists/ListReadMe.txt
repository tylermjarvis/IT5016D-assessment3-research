# Folder Title
StatePattern-Lists


# Folder Description
This folder analyses Python List and how they can be used within the State Method Pattern. List are a valuable way of holding data types that can be accessed
through the list's index. They are easy to loop through and manipulate. The State Method has been used in this folder, as a list allows us to hold data types
that can be changed depending on the state of an object.

There is a folder with the answers to Learning Activity 40. These answers have helped me conceptualise how lists can be navigated through via their indexes and
how stored data within them can be manipulated.

There is also a folder with all my practice code, carried out during the learning activities, which include comments and brief descriptions (some exercises) of why booleans are
used. The comments break down the problems so that they are easy to follow, as well as apply ideas on how the State Method may be used with these problems.

There is one Python file (StateMethodExample.py) that takes a Python Design Pattern example from GeeksforGeeks and applies it to how a specific Python syntax may be used with this pattern.
I also analyses this example, by breaking it down and explaining the scenario/problem that the pattern is solving, to get a better understanding of this particular 
Python Design Pattern. I then study how this pattern and the learning examples work towards following the Python design principles.
For example:
Using list operations with the State Method pattern which cater to the Open/Close Principle.


# More Information
Please look at the following Python code files and screenshots for more specific comments relating to each exercise and how specific examples relate to Python 
design principles and patterns.


# How Lists Work
my_list = ['p','r','o','b','e']
print(my_list[0])
print(my_list[2])
print(my_list[-1])

# Expected output "p" "o" "e"


# Context of Design Pattern
The State Method Pattern is a behavioural design pattern that allows us change an objects behaviour when there is a change in its internal state. We can use 
a state variable in the object and use conditional statements to decide its behaviour.

An advantage of the State Method Pattern is that we can introduce new states without changing the content of the existing state within the classes.


# Python Design Patterns
State Method Pattern - allows us to change the behaviour of an object using new states.