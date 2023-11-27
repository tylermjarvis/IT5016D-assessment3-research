# Exception3_WithAdditionalHandler.py
# @ author: Administrator
# Date: 2.11.23

# You can change the behaviour of the exception, so that the user can see why
# there is an exception being thrown
def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except (ZeroDivisionError, TypeError):
        return "Error, check your parameters!"
 
print(divide_numbers(3,0))
 
# Output
'''
Error, check your parameters!
'''

'''
In this example, we cover both exceptions that may occur when trying to divide
two numbers. We have the ZeroDivisionError error and the TypeError error, with a
message that caters to both errors, as both of these errors are to do with the
parameters. By throwing this exception we are using the Exception Error
Handling pattern to create a program that includes all outcomes.
'''
