# Project Title
IT5016D-assessment3-research


# About Project
This is Assessment 3 for the paper IT5016D Software Development Fundamentals. It includes my research and projects that I have carried out during my coding journey with Python.


# Motivation
This project has been created as a way to look back on the coding that I have learnt and the exercises I have completed using Python and the Software Development learning activities.
With these example exercises that I have used to practice and inspired code from online, I will delve into how programs can be created with common Python design patterns and principles.
The repo will also help me find specific coding blocks that I can refer to for future projects.


# Navigation
Each folder is broken down into the syntax of Python and the design patterns that I have chosen to work with that syntax. The syntax is used to develop the idea of how Python Design Patterns are used and the principles reinforce why we use design patterns. For example, creation patterns are explored within the Class folder, due to the initialisation stage being explored within creation patterns, and how each scenario can change the pattern we use to approach the problem. Each folder contains a Python file that explores a design pattern example from GeeksforGeeks with comments, a screenshot with a diagram on how this pattern works, a folder with practice code and comments, answers to the learning activities and a ReadMe with an over view of the folder and those design patterns used.

Folder structure:
AbstractFactoryPattern-Functions - Abstract Factory Pattern with functions.

AdapterPattern-Dictionary - Adapter Pattern with dictionaries.

BehaviouralPatterns-Tuples - Behavioural design patterns with tuples.

DecoratorPattern-Booleans - Decorator Pattern with booleans.

ExceptionHandlingPattern-Debugging - Exception Handling Pattern with debugging.

ExceptionHandlingPattern-Exceptions - Exception Handling Pattern with Python exceptions.

FactoryPattern-Classes - Creational patterns such as Factory method pattern and Facade pattern with classes.

IteratorPattern-Loops - Iterator Pattern with loops.

MediatorPattern-Strings - Mediator Pattern with strings.

StatePattern-Lists - State Pattern with lists.

StrategyPattern-NumericData - Strategy Pattern with numeric data.


# Common Python Design Patterns
Singleton pattern - This pattern restricts instantiation to just one instance of a class.

Factory method pattern - This is a creational pattern that uses a factory method to create objects without specifying the exact class of that object.

Abstract Factory method Pattern - allows us to create products without using instantiating classes. The factory class deals with this behaviour.

Adapter pattern - This pattern allows the interface (a class that defines methods that can be overridden) of a class to be used as another interface. It is used to make exisiting classes work with other classes, without changing their source code.

Builder pattern - The builder pattern is used to separate the construction of an object with multiple layers using a step by step build pattern.

Facade pattern - This pattern allows us to carry out subtasks within a class that can call these subtasks. Therefore acting as the face of this subsystem.

Decorator pattern - Uses decorator functions to wrap new behaviours over an object.

Exception Handling pattern - allows us to deal with errors throughout our program, and therefore test and debug more appropriately.

Iterator method pattern - allows us to loop through a data collection in a clean way that prevents the use of numerous loops.

Mediator method pattern - allows us to use a mediator to communicate between different objects.

State method pattern - allows us to change the behaviour of an object using new states.

Strategy method pattern - allows us to setup an an algorithm within functions that we can use to replace a method within a class.


# S.O.L.I.D and S.T.U.P.I.D Design Principles
SOLID:
- Single Responsibility Principle - blocks of code should only carry out one function.
- Open/Close Principle - Avoid coding that requires you to re-opening previous code blocks.
- Liskov Substitution Principle - Objects of a superclass should be able to be replaced with objects of a subclass, without causing problems with the program.
- Interface Segregation Principle - No code should be forced to depend on methods they do not use.
- Dependency Inversion Principle - High-level modules should not depend on low-level modules. Only depend on abstractions.

STUPID:
- Singleton - Restricts the instantiation of a class to one "single" instance.
- Tight Coupling - Coupling is when each program module relies heavily on each of the other modules.
- Untestability - Code should be testable.
- Premature Optimisation - Premature optimization is spending a lot of time on something that you may not actually need.
- Indescriptive Naming - Name classes, methods, attributes, and variables in a way that makes sense for what code they cater to and for the developer.
- Duplication - Don’t Repeat Yourself (DRY).


# My Learning Journey
While working through the learning activities, I often found myself relying on the answers after I had attempted the exercises. This helped me gain an understanding of how to think in Python and how the Python functions and syntax worked. As I progressed through the learning exercises, I started feeling more confident to complete the exercises by myself, due to seeing how the problem was broken down in the answers when I was first learning Python. I relied on the comments within my notes to help me understand new problems that I was attempting to solve. 
For the design patterns, I found GeeksforGeeks examples to be very helpful, due to the detail that the examples included when breaking down a problem. This is why I have decided to study their examples of design patterns in order to understand design principles, the advantages of using design patterns and what problems these patterns can be used for. I have also included screenshots of diagrams from these patterns that I found on the GeeksforGeeks site as they assisted with my understanding of design patterns.
By following the design patterns listed above, I have been able to break down how the design patterns lead to using SOLID design principles, such as the Single Responsibility Principle and the Open/Close Principle, while avoiding code within STUPID, such as Tight Coupling and Indescriptive Naming.
