# LA19_Baby.py
# @ author: Administrator
# Date: 17.10.23

'''
Random is a function that can be imported. It allows this program to access
a random selector based on the data type specified
'''
import random

'''
# Here we predefine male with a boolean type of False, then we flick between
False and True, using the numbers 0 and 1
'''
male = False
male = bool(random.randint(0, 1))

'''
This allows us to use the if conditional statement to change what code is
executed
'''
if (male):
   print ("We will use name Rangi")
else:
   print ("We will use name Anihera")


'''
The random import is helpful when executing a code block that meets a certain
condition and is imitating a random scenario.

If you wanted to decorate a block of code for a program based on a random
result, you could set the condition of a function to execute with the random
function. Therefore, this would create a program that might replicate a
situation where random acts are part of the scenario.
'''
