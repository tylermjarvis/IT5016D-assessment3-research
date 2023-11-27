# ExerciseC3_a.py
# author: Administrator
# date: 17/10/23

# import math as we need the square root function
import math

# user input
side_e = int(input("Please enter the length of side e\n\n"))
side_d = int(input("Please enter the length of side d\n\n"))

# calculation carried out within print
print("\nThe area of your shape is ",
      # half the base, times the height
      side_d / 2 * math.sqrt(side_e ** 2 - side_d ** 2)
      ,"\n\n")

# Testing
'''
print("My assertions are:"
      "\ne = 5, d = 4,  output = 6"
      "\ne = 25, e = 24,  output = 84")
'''

'''
Another design pattern is the Iterator Method pattern, which could be used here
to move through a collection of shape lengths and provide them as the input,
as opposed to the user input.
'''
