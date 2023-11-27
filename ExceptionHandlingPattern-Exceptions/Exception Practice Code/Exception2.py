# Exception2.py
# @ author: Administrator
# Date: 2.11.23

def divide_numbers(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return "Error, cannot divide by zero."

# A string has been added instead of a int - Therefore a TypeError will be raised
print(divide_numbers(3,"asdf"))
 
# Output
'''
2 Outputs:
TypeError: unsupported operand type(s) for /: 'int' and 'str' - Because we have
given divided numbers a string instead of an int

Or if we supply divide_numbers with a 3 and a 0 then we will get:
Error, cannot divide by zero.
'''

'''
In this example here, we are catering to an error when dividing by zero.
Although, because we have put a string as one of the parameters instead of a
numeric value, we receive a TypeError being thrown. The program expects a
numeric value.
This shows that there are numerous errors to think about and cater for. If
this was a larger program, finding a TypeError might be difficult, therefore
it is a good habit to use the Exception Error Handling pattern to anticipate
all outcomes, or have messages that explain what is required to avoid these
sorts of errors.

In this example we could use a conditional statement to determine what error is
triggered whilst the program is running. We could have the TypeError exception
and the ZeroDivisionError exception.
There is another solution used in the next exercise.
'''
