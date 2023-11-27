# ExerciseC2_b.py
# author: Administrator
# date: 17/10/23

# import math as we need math.pi for a circle
import math

# user input for circle radius
side_x = int(input("Please enter the radius of the circle\n\n"))

# calculation carried out within print
print("\nThe area of your shape is ", side_x ** 2 * math.pi * 3/4 ,"\n\n")

# Testing
'''
print("My assertions are:"
      "\nx = 5, output = 58.9"
      "\nx = 7, output = 115.5")
'''

'''
Here we are calculating the area of a circle which uses pi times diameter.
This design can be used with the Strategy Pattern, in the same way that
exercises in C1 can use it, however the standard class would have the base code
for calculating areas of circular objects.
'''
