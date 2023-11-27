# ExerciseC3_c.py
# author: Administrator
# date: 17/10/23

# import math as we need the square root function
import math

# user input
side_g = int(input("Please enter the length of side g\n\n"))
side_e = int(input("Please enter the length of side e\n\n"))

# find the missing length for the triangle
side_new = side_g / math.cos(math.radians(38))

# calculation carried out within print
print("\nThe area of your shape is ",
      side_new / 2 * side_g
      + side_e * side_g
      + (side_g/2) ** 2 * math.pi/2
      ,"\n\n")

# Testing
'''
print("My assertions are:"
      "\ng = 6, e = 6, output = 72.98"
      "\ng = 7, e = 2, output = 64.33")
'''

'''
When looking for the missing length of a shape, we could use the Strategy Method
pattern to have a method that is replaced with a function that allows us to
calculate the missing length and therefore we have a function that has a
single responsibility, as opposed to having the shape class that stores all
shape values, dealing with the calculation.
'''
