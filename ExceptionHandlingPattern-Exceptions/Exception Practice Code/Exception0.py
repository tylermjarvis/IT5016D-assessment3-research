# Exception0.py
# @ author: Administrator
# Date: 2.11.23

# "Cannot divide by zero" is returned as we cannot divide by zero
def divide_numbers(number_1, number_2):
    if number_2 == 0:
        return "Cannot divide by zero."
    return number_1 / number_2
 
print(divide_numbers(3,0))
 
# Output
'''
Cannot divide by zero.
'''

'''
A Python exception is used in the later exercises, but we can see that there
should be a case/return for an undesired result (bad outcome).
'''
