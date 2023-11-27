# BoolTests.py
# @ author: Administrator
# Date: 17.10.23

# Using print to see the different results with the bool data type
print ("Test 1 ", bool(True)) # True = True
print ("Test 2 ", bool(False)) # False = False
print ("Test 3 ", bool("text")) # string with characters = True
print ("Test 4 ", bool("")) # string with no characters = False
print ("Test 5 ", bool(" ")) # string with space character = True
print ("Test 6 ", bool(0)) # 0 = False
print ("Test 7 ", bool())# nothing = False
print ("Test 8 ", bool(3)) # number greater than 0 = True
print ("Test 9 ", bool(None)) # None has the value of False

'''
These examples can be used in a variety of ways to execute blocks of code that
require user input with a variety of data types.
For example you can have a conditional statement that runs if the value is 0 or 3
or if the input meets a specific string, string length or an empty string.

These could be a variety of conditions that may be used in the conditional
decorator pattern in order to change the behaviour of a program and decorate
the data in a different block of code.
'''
