# Folder Title
AdapterPattern-Dictionary


# Folder Description
This folder includes dictionaries and Python design patterns and principles that allow for the most efficient way to update an object using dictionaries. Dictionaries
hold keys and their values, which can be called using the {} symbol. The important thing about dictionaries is that the key is a unique name that cannot be repeated. Using the
key you can update the dictionary with new values. One Python design pattern that is explored in depth here is the Adapter method pattern. There are coding examples 
within this file that introduce the basics of dictionaries and how they can use the Adapter method to update objects.

There is a folder with the answers to Learning Activities 43 and 44s, which has been included in the dictionary folder, due to it assisting my learning of dictionaries 
in Python. These answers have helped me break down the exercises into an understandable process.

There is also a folder with all my practice code, carried out during the learning activities, which include comments and brief descriptions (some exercises) of why dictionaries are
used. The comments break down the problems so they that are easy to follow, as well as apply ideas on how the Adapter Method may be used with these problems.

There is one Python file (AdapterMethodExample.py) that takes a Python Design Pattern example from GeeksforGeeks and applies it to how a specific Python syntax may be used with this pattern.
I also analyses this example, by breaking it down and explaining the scenario/problem that the pattern is solving, to get a better understanding of this particular 
Python Design Pattern. I then study how this pattern and the learning examples work towards following the Python design principles.
For example:
Using Dictionaries with the Adapter Method pattern and how it can cater to the Single Responsibility Principle.


# More Information
Please look at the following Python code files and screenshots for more specific comments relating to each exercise and how specific examples relate to Python 
design principles and patterns.


# How Dictionaries Work
states = {
    'Oregon': 'OR', # Here you have a key "Oregon" and it's value "OR"
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}


# Context of Design Pattern
To use the Adapter method design pattern, we first create the class that the adapter will adapt to. Then we set the adapter methods in the object's dictionary, in order
to update the object instance. Then we pass all non-adaptered calls to the object as well. Finally we can print the object dictionary and call it using:
objects = []
objects.append(Adapter(className, replacedMethod.method))

An advantage of the adapter method pattern is that we can use the principle of single responsibility, because we can separate the creation code from the 
main logic. It helps with reusability of the code. We also don't break the open/close principle as we can adapt to classes using the adapter class and therefore not touch
the main class.
A disadvantage is that adding more adaptions adds to the complexity of the code.

Dictionaries are used to store data in Python in the form of a key and it's value. Therefore design patterns relating to dictionaries involve the use of updating
objects and content of a class object.

For reference see, the following link:
https://www.geeksforgeeks.org/adapter-method-python-design-patterns/


# Python Design Patterns Studied
Adapter Pattern - Adapt methods or incompatible objects to each other through adaptability.