# Folder Title
IteratorPattern-Loops


# Folder Description
This folder discusses Python Loops and how they go hand and hand with the Iterator Method Pattern. Loops are how we search through a particular data type, such as lists and 
dictionaries. We do this with "for" loops. We can also use "while" loops that loop through a block of code until a certain condition is met. While we are looping, we need a way
to exit that loop. The Iterator Method allows us to move through a group of data types or collections, without going in-depth into those collections and therefore saving memory. 
It allows us to access complex data collections and structures sequentially without repeating data, due to the continues movement or iteration of the loop.

There is a folder with the answers to Learning Activities 37 and 38. These answers have helped me conceptualise how loops use iterators to navigate through data collections
and return the desired results of that collection.

There is also a folder with all my practice code, carried out during the learning activities, which include comments and brief descriptions (some exercises) of why loops are
used. The comments break down the problems so that they are easy to follow, as well as apply ideas on how the Iterator Method may be used with these problems.

There is one Python file (IteratorMethodExample.py) that takes a Python Design Pattern example from GeeksforGeeks and applies it to how a specific Python syntax may be used with this pattern.
I also analyses this example, by breaking it down and explaining the scenario/problem that the pattern is solving, to get a better understanding of this particular 
Python Design Pattern. I then study how this pattern and the learning examples work towards following the Python design principles.
For example:
Using loop operations with the Iterator Method pattern which cater to the Open/Close Principle.


# More Information
Please look at the following Python code files and screenshots for more specific comments relating to each exercise and how specific examples relate to Python 
design principles and patterns.


# How Loops Work
number = int(input("Please type a number...\n"))
count = 0
total = 0

while count <= number:
    total = total + count
    count += 1

print("number =", number, "sum =", total, "\n")


# Context of Design Pattern
The Iterator Method Pattern is a behavioural design pattern that allows us to move through a loop to receive specific data. To achieve this we use the common practice of have
an i represent the iterator that will move through the loop. It is similar to incrementing, as the i moves through the collection, one data piece at a time.

An advantage of the Iterator Method Pattern is that it is easier to extract data from huge collections using seperate iterator classes, therefore following the Single
Responsibility Principle. It prevents us from breaking previous code, due to enter this data collection without changing the collection itself. Therefore, we also follow
the Open and Close Principle.


# Python Design Patterns
Iterator Method Pattern - allows us to loop through a data collection in a clean way that prevents the use of numerous loops.