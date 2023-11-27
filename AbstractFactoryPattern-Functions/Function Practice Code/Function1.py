# Function1.py
# @ author: Administrator
# Date: 30.10.23
 
def show_my_message():
    print("Gidday mate, this is a simple function as it does not take any parameters. It does however print this text!!!\n\n")
 
print("Testing my first user defined function...\n\n")
 
# invoking the function
show_my_message()
 
# invoking the function again
show_my_message()

# Functions can be called over and over

 
'''
Testing my first user defined function...
 
Gidday mate, this is a simple function
as it does not take any parameters. It does however print this text!!!
 
Gidday mate, this is a simple function
as it does not take any parameters. It does however print this text!!!
'''

'''
This example is the beginning of breaking down functions and how they can work
with the Abstract Factory Method. Because we can call functions from anywhere
in the code block, we can use this to setup how the Abstract Factory Method
is carried out. The Abstract Factory pattern requires the use of a factory
class that instantiates other classes, therefore the way to send that
information from the classes to the factory class is through functions, or
more specifically, methods (Similar to functions).
