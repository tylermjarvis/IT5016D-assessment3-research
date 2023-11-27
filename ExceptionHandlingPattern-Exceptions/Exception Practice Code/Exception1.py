# Exception1.py
# @ author: Administrator
# Date: 2.11.23

# An exception is thrown as we have supplied the exception ZeroDivisionError
def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Error, cannot divide by zero!"
 
print(divide_numbers(3,0))
 
# Output
'''
Error, cannot divide by zero!
'''

'''
In this example we are using the Python exception called ZeroDivisionError.
This exception, throws an error if the number supplied is zero.
It is important to note that there is a message with this error so that
the user/developer can understand why the error has occured. This is using the
Exception Error Handling pattern, due to the use of Python exceptions in the
program. This makes the program more user friendly, as well as caters to errors
that we are aware of, therefore making it easier to follow the code, refactor
the code or debug problems.
'''
