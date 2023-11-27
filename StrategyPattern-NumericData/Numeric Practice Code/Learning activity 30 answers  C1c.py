# ExerciseC1_c.py
# author: Administrator
# date: 17/10/23

# user input for a shape that is not a standard shape
side_u = int(input("Please enter the length of the rectangle\n\n"))
side_m = int(input("Please enter the width of the rectangle\n\n"))
side_n = int(input("Please enter the length of the side of the triangle\n\n"))

# calculation carried out within print
print("\nThe area of your shape is ",
      side_u * side_m
      + side_n / 2 * side_n
      ,"\n\n")

# Testing
'''
print("My assertions are:"
      "\nu = 5, m = 3, n = 5 output = 27.5"
      "\nu = 2, m = 1, n = 5 output = 14.5")
'''

'''
Here we are calculating a shape that is not a standard rectangle or triangle,
therefore the calculations to do this are different. We must calculate the shape
with both a rectangle and a triangle calculation and add them together.

This design can be used with the Strategy Pattern, in the same way that exercise
C1 a and C1 b can use it.
'''
