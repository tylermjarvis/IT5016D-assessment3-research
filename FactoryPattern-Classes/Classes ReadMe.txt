# Folder Title
FactoryPattern-Classes


# Folder Description
This folder includes classes and Python design patterns and principles that make more efficient use of classes, in a way that makes them more reusable and tidy. Classes in
Python are used to create objects that hold data, which relate to a specific topic, e.g. a persons name, age, date of birth, address. One Python design pattern that is 
explored in depth here is the Factory design pattern. There are coding examples within this file that introduce the basics of classes and how they can use the Factory Method
to create new types of products without changing/updating the existing class and it's base code/initializer. 

There is a folder with the answers to Learning Activity 61, Classes and Objects, which has been included in the class folder, due to it assisting my learning of classes
and objects in Python. It has helped me break down the exercises into an understandable process.

The Classes and Objects exercise is in a folder called Classes Practice Code. This file includes comments and brief descriptions (some exercises) of why classes are
used. The comments break down the problems so that they are easy to follow, as well as apply ideas on how the Factory Method and Facade Method may be used with these problems.

There is two Python files (FactoryPatternExample.py and FacadePatternExample.py) that takes a Python Design Pattern example from GeeksforGeeks and applies it to how a 
specific Python syntax may be used with this pattern.
I also analyses this example, by breaking it down and explaining the scenario/problem that the pattern is solving, to get a better understanding of this particular 
Python Design Pattern. I then study how this pattern and the learning examples work towards following the Python design principles.
For example:
Using classes with the Factory Method pattern which cater to the Single Responsibility Principle.


# More Information
Please look at the following Python code files and screenshots for more specific comments relating to each exercise and how specific examples relate to Python 
design principles and patterns.


# Context of Design Pattern
Because the Factory method creates new types of products without changing/updating the existing class base code/initializer. It is therefore more efficient as we avoid 
tight coupling between the new products and the classes that are creating them through the Factory method. A disadvantage of this is that in order to create new product, 
we will have to create a sub-class of the class initializing the object to access the creation of this new product.
See the link below for a reference to the Factory pattern and the advantages and disadvantages.
https://www.geeksforgeeks.org/factory-method-python-design-patterns/

Factory pattern screenshot example from
https://refactoring.guru/design-patterns/factory-method/python/example


# How Classes Work
class Person:
    # Initialize the object values
    def __init__(self, age, gender, address, height):
        self.age = age
        self.gender = gender
        self.address = address
        self.height = height

    def myIntro(self):
        print("Hello my gender is " + self.gender)
        print("Hello my age is", self.age)
        print("Hello my address is " + self.address)
        print("Hello my height is", self.height)

harry = Person(36, "male", "10 Garden Ave, Auckland", "167cm")

harry.myIntro()


# Context of Design Patterns
Classes are used with all the Python design patterns, as they initialize objects for Python to manipulate. They are
mainly used with Creational patterns, due to their instantiation of Python objects.
An example of this is the Singleton Pattern, which restricts the instantiation of a class to one instance only.


# Python Design Patterns Studied
Factory Method Pattern - Allows us to instantiate an object of a class without specifying that class.
Facade Pattern - This allows us to carry out subtasks within a class that can call these subtasks. The class calling
the subclass acts as a face for these tasks, but does not update or change anything itself.

