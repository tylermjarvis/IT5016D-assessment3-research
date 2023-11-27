# ExerciseC3_b.py
# author: Administrator
# date: 17/10/23

# import math as we need the cosine value of a number and the radian
import math

# user input
side_f = int(input("Please enter the length of side f\n\n"))

# calculation carried out within print
print("\nThe area of your shape is ",
      # half the base, times the height
      side_f / 2 * side_f * math.cos(math.radians(40))
      ,"\n\n")

# Testing
'''
print("My assertions are:"
      "\nf = 5, output = 9.6"
      "\ne = 7, output = 18.8")
'''
