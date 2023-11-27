# Folder Title
BehaviouralPatterns-Tuples


# Folder Description
This folder analyses Python Tuples and how they can be used to protect data from behavioural patterns, due to being immutable. Tuples are similar to lists,
as they store data within a specific order. However this data is protected as it cannot be changed. Therefore this folder delves into the idea of using
Tuples to protect objects whilst using behavioural design patterns that can change the data during runtime. Protecting data is always important while 
creating a program as it prevents the program from breaking when a change is made, hence why the principle Open/Close is very important. The more we refactor
previous code, the more chances we have of breaking that program. The practice code breaks down how Tuples work and my learning journey while working with
Python's Tuples.

There is a folder with the answers to Learning Activity 42. These answers have helped me conceptualise how tuples can be used to protect ordered data.

There is also a folder with all my practice code, carried out during the learning activity, which include comments and brief descriptions of why tuples are
used. The comments break down the problems so that they are easy to follow, as well as apply ideas on how tuples may protect data within behavioural design 
patterns.


# More Information
Please look at the following Python code files and screenshots for more specific comments relating to each exercise and how specific examples relate to Python 
design principles and patterns.


# What Is A Tuple
bank_accounts = (("Joe", 33, "234 Great South Road", "022629107"),
                 ("Tama", 6000),
                 ("Suzanne", 21025, "45 Green Lane"),
                 ("Anihera", -75))


# Context of Design Pattern
Behavioural design patterns allow us change an objects behaviour during runtime. They include Chain of Responsibility, Command Method, Iterator Method,
Mediator Method, Memento Method, Observer Method, State Method, Strategy Method, Template Method and Visitor Method.

The advantage of using Tuples with these methods, is that we can protect data as it flows through these patterns at runtime.