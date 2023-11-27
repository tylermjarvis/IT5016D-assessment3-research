# ForLoopExercises.py
# @ author: Administrator
# Date: 25.10.23

# grab number to loop through
user_input = int(input("Please enter the number of times that you wish to see the message."))

# for loop with i to iterate up to the user input number
for i in range(user_input):
    print("hello world....", i)

# user input number
user_input = int(input("Please enter a number for the size of the shape you wish to create."))

# iterates until the user input number to place *
for i in range(user_input):
    for j in range(i):
        print('* ', end="")
    print('')

# iterates until the end of the user input number to place *
for i in range(user_input, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')

'''
Here we can see the use of the Iterator Method Pattern in a simple for loop.
We have not used an iterator class, however the use of i, being the iterator in
the for loops is how the Iterator Method pattern achieves the ability to search
through data collections of various functions.

For example, if we were to have a data collection that we wanted to print
numerous times, we would follow the for loop with the iterator (i) in the first
exercise. However this would be in its own Iterator function, which calls the
datacollection of another class.
These coding practice examples feature the use of for looping with an iterator
in order to print data (hello world.... and * in the form of a shape). Therefore
we can see from these examples that an iterator can be used to print data. We
can then use this with the Iterator Method to print data using iterator
functions. This is important as we are able to take data from collections in
other classes or functions and print that data, therefore following the
Open/Close Principle, as we can take that data without touching that collection.
'''

