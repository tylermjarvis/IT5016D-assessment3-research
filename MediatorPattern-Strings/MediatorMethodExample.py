# MediatorMethodExample.py
# @ author: Administrator
# Date: 24.11.23

class Course(object):
    # Mediator class.
    def displayCourse(self, user, course_name):
        print("[{}'s course ]: {}".format(user, course_name))
 
 
class User(object):
    # A class whose instances want to interact with each other.
    def __init__(self, name):
        self.name = name
        self.course = Course()
 
    def sendCourse(self, course_name):
        self.course.displayCourse(self, course_name)
 
    def __str__(self):
        return self.name
 
# main method
if __name__ == "__main__":
    mayank = User('Mayank')   # user object
    lakshya = User('Lakshya') # user object
    krishna = User('Krishna') # user object
 
    mayank.sendCourse("Data Structures and Algorithms")
    lakshya.sendCourse("Software Development Engineer")
    krishna.sendCourse("Standard Template Library")

'''
Seen in this example from GeeksforGeeks, the Mediator Method is used when you
want to have class instances to interact with each other. The problem with this
example is that you may have courses on offer that weren't popular at the start,
therefore it was easy to create separate objects and classes. However, as the
courses become more popular, it becomes harder for developers to handle lots
of sub classes (courses). So here we can create a class that the students
and the courses talk to. It is the communicator between the two. The mediator
class (Course) has a method called displayCourse which is communicating to the
User method called sendCourse. This is possible as the User class takes the
Course class in it's initialiser. Then all we need to do is send the student
information (name and course) through the main method to the sendCourse method.
This sendCourse method then talks to Course to link the student with the course
they are taking.
The advantage of using this pattern is that we are assigning single
responsibility to extract communication between all elements. This makes it
easier to maintain. We also allow for inheritance, which means the code is
reusable. These are both principles to follow for efficient code.

By catering for inheritance and single responsibility, we can use what we have
learnt in the practice code with strings and apply this to the mediator class.
We can use string methods, such as find(), startswith(), concatenation,
splitting and joining to apply string manipulation to a number of class objects
through the mediator class that is communicating with them. In this example we
could captialise the student name so that it is filed in a way that is
understandable in a database.
'''
