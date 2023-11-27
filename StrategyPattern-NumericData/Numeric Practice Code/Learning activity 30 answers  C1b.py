# ExerciseC1_b.py
# author: Administrator
# date: 17/10/23

# all user input for rectangle sides
side_q = int(input("Please enter the length of the small rectangle\n\n"))
side_w = int(input("Please enter the width of the small rectangle\n\n"))
side_s = int(input("Please enter the length of the large rectangle\n\n"))
side_g = int(input("Please enter the width of the large rectangle\n\n"))

# calculation carried out within print
print("\nThe area of your shape is ", side_g * side_s - side_q * side_w,"\n\n")

# Testing
'''
print("My assertions are:"
      "\nq = 5, w = 3, s = 8, g = 4 output = 17"
      "\nq = 2, w = 1, s = 5, g = 3 output = 13")
'''

'''
The example above uses user input to calculate a rectangle with a standard
rectangle calculation of side_1 times side_2 times side_3 times side_4.
The Strategy Method Pattern can be used here like exercise C1 a as a way to
calculate a variety of shapes or rectangles under one class. This class uses
functions to replace it's methods, depending on what shape is being calculated.
The Strategy Method is used when you have a base calculation that is
required to be carried out by another calculation.
'''
