# AbstractFactoryMethod.py
# @ author: Administrator
# Date: 22.11.23
 
import random
 
class Course_At_University:
    # Factory for courses
    def __init__(self, courses_factory = None):
        # course factory is our abstract factory
        self.course_factory = courses_factory
 
    def show_course(self):
        # creates and shows courses using the abstract factory
        course = self.course_factory()
 
        print(f'We have a course named {course}')
        print(f'its price is {course.Fee()}')
 
 
class DSA:
    # Class for Data Structure and Algorithms
    def Fee(self):
        return 11000
 
    def __str__(self):
        return "DSA"
 
class STL:
    # Class for Standard Template Library
    def Fee(self):
        return 8000
 
    def __str__(self):
        return "STL"
 
class SDE:
    # Class for Software Development Engineer
    def Fee(self):
        return 15000
 
    def __str__(self):
        return 'SDE'
 
def random_course():
    # A random class for choosing the course
    return random.choice([SDE, STL, DSA])()
 
if __name__ == "__main__":
 
    course = Course_At_University(random_course)
 
    for i in range(5):
        course.show_course()

'''
Seen here in this example are methods, called Fee and __str__. Although they are
not functions, they work in similar ways to functions, but are bound to
classes and objects.
We have a factory class called Course_At_University, within the Abstract Factory
Method. This class creates a course factory which has a method that assigns course
to this initialisation when called. In the same way that a return function works, we
assign the returned object creation (course_factory) to courses, which will access
each course class.
We then have a number of classes with a Fee method that returns a price and a __str__
method that returns an acronym. We can then use the variable course to assign
the class Course_At_University(random_course) and give it the parameter of a random
list. We can see through this factory variable of course, that we are able to
link all of these course classes within one class that is controlling the creation
of the courses.

This helps us deal with any scenario where we may want to instantiate a number
of objects but we do not want to change their code and we may want to add more
products, therefore we do not want to manually instantiate them, due to time and
memory cost.
The practice functions in the practice code examples, help to build an idea of how
you can use functions in a similar manner, to achieve the outputs
required by the program. The practice code functions include get functions,
parameter functions and many other functions that can help us use the Abstract
Factory class to create objects. An example of this is how we send data to other
classes, using the idea of a function.

I have been inspired by this piece of code due to it's ability to break down
the Abstract Factory Method into a simple code program that explains, what the
problem is set out to resolve, why we use this design pattern and the advantages
and disadvantages of this pattern.
'''

