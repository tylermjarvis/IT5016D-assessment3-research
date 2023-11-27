# ExerciseC1_a.py
# author: Administrator
# date: 17/10/23

# user input for triangle calculation
side_j = int(input("Please enter the length of the base of the triange\n\n"))
side_k = int(input("Please enter the perpendicular height of the triange\n\n"))

# calculation carried out within print
print("\nThe area of your triange is ", side_j / 2 * side_k,"\n\n")

# Testing
'''
print("My assertions are:"
      "\nj = 5, k = 4 output = 10"
      "\nj = 7, k = 9 output = 31.5")
'''

'''
The example above uses user input to calculate a triangle with a standard
triangle calculation of side_1 divided by 2 times side_2.
The Strategy Method Pattern can be used here as a way to calculate a variety of
shapes under one class. This class uses functions to replace it's methods,
depending on what shape is being calculated.
The Strategy Method is used when you have a base calculation that is
required to be carried out by another calculation.
'''
