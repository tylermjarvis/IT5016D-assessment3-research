# LA61_ClassesAndObjects.py
# @ author: Administrator
# Date: 07.11.23
 
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

# Create the object
harry = Person(36, "male", "10 Garden Ave, Auckland", "167cm")

# Calling the method myIntro, using the object harry
harry.myIntro()

# output
'''
Hello my gender is male
Hello my age is 36
Hello my address is 10 Garden Ave, Auckland
Hello my height is 167cm
'''

'''
How can this be used with Python design patterns?

This code gives you the base to start the Factory design pattern, due to the
initialization of the class object.
We can use this code with the Factory design pattern to read from a csv file
with multiple data entries, using from_csv_line as a class method. This
allows us to use functions such as map, which create a simplistic way of
creating objects due to the Factory design. The Factory pattern works well
with database and json data from APIs. It simplifies how we use
and how we create objects from a file with predefined data.
It is important to note that we reduce coupling by adding these features, as the
Factory Method is designed to make it easier to refactor code without having
to refactor code that is dependent on the other code. This goes hand and hand
with the Single Responsibility Principle that reduces coupling due to each
function carrying out its own task.
'''

'''
For example, the following code uses the Factory design pattern, which would
retrieve data entries from a csv file:

class Person:
    # Initialize the object that will be created with the data from the csv file
    def __init__(self, name, age, university, degree):
        self.name = name.title()
        self.age = age
        self.university = university.title()
        self.degree = degree.capitalize()

    # This class method is reading each line in the csv file and spliting it via
    # the commas. It is also the factory method that will create the objects
    @classmethod
    def from_csv_line(cls, line: str):
        return cls(*line.split(",")) # The *line grabs additional returns from
                                     # the line

# readlines() method returns a list with each line in the file as a list item
with open("csv_data.text", "r") as file: # The r means that the file should be
    lines = file.readlines()             # opened in read mode

# lines[1:] creates a slice of the lines list which begins at index 1
lines = [line.strip() for line in lines[1:]] # strip removes whitespace

# The creates the objects and puts them into person_list
# person_list = [Person(*line.split(","))for line in lines] # map is a better function

# map allows us to generate objects and put them within a list
# Here we call the factory method to create the objects from the csv file
person_list = map(Person.from_csv_line, lines)

# print the list using the class initializer
for person in person_list:
    print(
        f"{person.name} is {person.age}, studying {person.degree} at {person.university}."
        )
'''

'''
The following link is a reference to this example on how to use the Factory
design pattern:
https://www.youtube.com/watch?v=JIImCgkAQxY
'''



