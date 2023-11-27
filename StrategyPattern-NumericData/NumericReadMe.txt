# Folder Title
StrategyPattern-NumericData


# Folder Description
This folder looks at Numeric data and how they can be used within multiple Python Patterns, due to it being a prominent data type in Python. Numeric data is used to
calculate data involving mathematical calculations within a program. Python patterns can be used to organise the calculation and returning of numeric data into code blocks that
are efficient, tidy and follow the Python principles, such as the Open/Closed Principle and the Single Responsibility Principle. There will be two Python 
Patterns that will be explored in this folder, along with how numeric data can be used with these patterns. The main pattern being explored is the Strategy Method Pattern,
and numeric data being used for multiple store discounts. Although the Iterator Method Pattern, is just as important, because Python must have a number value for interation. 
The collection data can be various data types, but the iterate must have a numeric value.

There are numerous Python files with the answers to the Learning Activity 30. These answers have helped me conceptualise how numeric data can be used to display
and calculate coding problems. There are a variety of data types that are numeric, including integer, float and complex.

The answers are located in the Numeric Practice Code folder, along with the other practice code carried out during the learning activities. They include 
comments and brief descriptions (some exercises) of why numeric data is used. The comments break down the problems so that they are easy to follow, as well as apply 
ideas on how the Strategy Method may be used with these problems.

There is one Python file (StrategyMethodExample.py) that takes a Python Design Pattern example from GeeksforGeeks and applies it to how a specific Python syntax may be used with this pattern.
I also analyses this example, by breaking it down and explaining the scenario/problem that the pattern is solving, to get a better understanding of this particular 
Python Design Pattern. I then study how this pattern and the learning examples work towards following the Python design principles.
For example:
Using numeric data types with the Strategy Method pattern which cater to the Single Responsibility Principle.


# More Information
Please look at the following Python code files and screenshots for more specific comments relating to each exercise and how specific examples relate to Python 
design principles and patterns.


# How Numeric Data Works
print ("Welcome to the Sleep Calculator\n")
user_yob = int(input("Please enter your year of birth...\n"))

# Calculate using integers
days_slept = user_yob * 365
sleep_total = days_slept * 7
 
# Print calculation result
print("Thank you for your input\n")
print("Your age in years is ", 2023 - user_yob)
print("This is how many hours you have slept ", sleep_total)


# Context of Design Pattern
The Iterator Method Pattern is a behavioural design pattern that allows us to move through a loop to receive specific data. To achieve this we use the common practice of have
an i represent the iterator that will move through the loop. It is similar to incrementing, as the i moves through the collection, one data piece at a time. Incrementing
and an iterator both require a numeric data type (integer for an iterator) in order to count through a collection.

An advantage of the Iterator Method Pattern is that it is easier to extract data from huge collections using seperate iterator classes, therefore following the Single
Responsibility Principle. We can enter this data collection without changing the collection itself, which prevents us from breaking the code as we have used the Open and Close Principle.

The Strategy Method Pattern is a behavioural design pattern that allows you to define algorithms and put them into separate classes. You can also change their objects. It is 
carried out through Python by replacing the content of a method in a class dynamically, with a function that is defined outside of this class. It enables us to select the 
algorithm we need at runtime.

A advantage of the Strategy Method Pattern is that we can isolate the implementation details of the code we require/algorithm, by using the class code. 


# Python Design Patterns
Iterator Method Pattern - allows us to loop through a data collection in a clean way that prevents the use of numerous loops.
The Strategy Method Pattern - allows us to setup an an algorithm within functions that we can use to replace a method within a class.