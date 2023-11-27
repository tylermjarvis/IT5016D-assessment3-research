# Signatures1.py
# @ author: Administrator
# Date: 31.10.23

 # function that takes away from the calling parameter
def show_young_age(my_age):
    print("My age 10 years ago was {0}.\n"
          .format(my_age - 10))
# invoking function
show_young_age(22) # 22 is the given age parameter

# output = My age 10 years ago was 12.

'''
Seen in this exercise, we could use the above calculation to manipulate data
that we have given to the function. For example the parameter my_age (22) will
be given to print, which will minus 10 to give the final result. We could
use this to change the data within the classes that are being sent to the
Abstract Factory class. We may want to do a calculation within these classes
and then get the factory class to instantiate these objects after the
calculation has been carried out. Maybe we need to calculate the discount price
of an item before we instantiate it with the factory class.
'''
