# ExerciseC2_c.py
# author: Administrator
# date: 17/10/23

# import math as we need math.pi for a circle
import math

# user input
side_g = int(input("Please enter the length of side f\n\n"))
side_e = int(input("Please enter the length of side g\n\n"))
side_f = int(input("Please enter the length of e\n\n"))

# calculation carried out within print
print("\nThe area of your shape is ",
      side_f / 2 * side_g
      + side_e * side_g
      + (side_g/2) ** 2 * math.pi/2
      ,"\n\n")

# Testing
'''
print("My assertions are:"
      "\ng = 6, e = 6, f = 6, output = 68.14"
      "\ng = 7, e = 2, f = 9, output = 64.74")
'''

'''
This design can be used with the Strategy Pattern, in the same way that
exercises in C1 can use it, however the standard class would have the base code
for calculating areas of shapes that are not standard shapes.
'''
