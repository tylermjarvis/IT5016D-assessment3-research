# Exception4_WithErrorMessage.py
# @ author: Administrator
# Date: 2.11.23

# You can supply more than one error message based on the exception that has been
# raised
def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Error, cannot divide by zero."
    except TypeError as e:
        message = "Error, an operand is the wrong type...\n" \
               "Or as Python would say...\n{0}".format(e)
        return message
 
print(divide_numbers(3,"Four"))

# Output
'''
Each exception type has its own handler.
This means that each error can be dealt with differently.
Notice too that the exception object can be called upon to provide the
Python error message. This is shown in the code as:
except TypeError as e:

C:\Users\willj\AppData\Local\Programs\Python\Python35-32\python.exe C:/Users/willj/PycharmProjects/PPCheckPoint1/PkgCheckPoint2/Exception3.py
Error, an operand is the wrong type...
Or as Python would say...
unsupported operand type(s) for /: 'int' and 'str'
 
Process finished with exit code 0
'''

'''
We can use e to represent the error as a message, that displays both the Python
error message and our own error message that helps the user understand the
error.
'''
