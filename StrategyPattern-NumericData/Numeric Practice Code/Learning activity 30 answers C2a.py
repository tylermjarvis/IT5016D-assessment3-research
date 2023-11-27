# ExerciseC2_a.py
# author: Administrator
# date: 17/10/23

# input for area of rectangle
side_x = int(input("Please enter the length of the rectangle\n\n"))
side_y = int(input("Please enter the width of the rectangle\n\n"))

# calculation carried out within print
print("\nThe area of your shape is ", side_x * side_y,"\n\n")

# Testing
'''
print("My assertions are:"
      "\nx = 5, y = 3, output = 15"
      "\nx = 7, y = 6, output = 42")
'''

'''
Here we are calculating the area of a shape which uses length times width.
This design can be used with the Strategy Pattern, in the same way that
exercises in C1 can use it, however the standard class would have the base code
for calculating shape area.
'''
