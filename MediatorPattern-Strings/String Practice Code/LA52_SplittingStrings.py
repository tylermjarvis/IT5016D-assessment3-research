# LA52_SplittingStrings.py
# @ author: Administrator
# Date: 2.11.23

# Challenge 1 - take 3 integers spearated by commas and find their average
user_input = input("Please enter 3 integers seperated by commas\n")
split_input = user_input.split(",")

# change string list to integer list
integer_list = [int(i) for i in split_input]

average = sum(integer_list)/len(integer_list)
print(average)

# test assertions
'''
user_input = 5,7,8
output = 6.666666666666667
user_input = 3,9,15
output = 9.0
'''


# Challenge 2 - take 3 integers spearated by commas and find their sum
user_input = input("Please enter integers seperated by commas\n")
split_input = user_input.split(",")

# change string list to integer list
integer_list = [int(i) for i in split_input]

sum_of_numbers = sum(integer_list)
print(sum_of_numbers)

# test assertions
'''
user_input = 7,4,12,14
output = 37
user_input = 23,28,39
output = 90
'''


# Challenge 3 - using shuffle() to jumble a sentence
from random import shuffle

stored_sentence = "This is a stored sentence that will be shuffled"
split_sentence = stored_sentence.split()

shuffle(split_sentence)
print(split_sentence)

# test assertions
'''
input = This is a stored sentence that will be shuffled
output = ['sentence', 'that', 'will', 'a', 'stored', 'be', 'is', 'shuffled', 'This']
input = This is a stored sentence that will be shuffled
output = ['is', 'will', 'a', 'This', 'stored', 'shuffled', 'be', 'sentence', 'that']
'''


# Challenge 8 - reverse string if it is a multiple of 4
string = "This string could possibly be a multiple of four"

def get_reversed(string):
    if len(string) % 4 == 0:
        string_reversed = "".join(reversed(string))
        return string_reversed
    else:
        return string
    
print(get_reversed(string))

# test assertions
'''
input = This string could possibly be a multiple of four
output = ruof fo elpitlum a eb ylbissop dluoc gnirts sihT
'''


# Challenge 11 - calculate numerous values of different shapes
# import math to have access to pi
import math

# square perimeter
def get_square_perimeter(side):
    perimeter = side * 4
    return perimeter

# triangle perimeter
def get_triangle_perimeter(side):
    perimeter = side * 3
    return perimeter

# circle perimeter
def get_circle_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter

# square area
def get_square_area(side):
    area = side ** 2
    return area

# triangle area
def get_triangle_area(side):
    area = (side / 2) * side
    return area

# circle area
def get_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

# cube volume
def get_cube_volume(side):
    volume = side ** 3
    return volume

# tetrahedron volume
def get_tetrahedron_volume(side):
    volume = (side ** 3) / 6 * math.sqrt(2)
    return volume

# sphere volume
def get_sphere_volume(radius):
    volume = 4 / 3 * math.pi * (radius ** 3)
    return volume

# user input for calculations
user_input = input("Please type either square, triangle or circle followed by a comma, then volume, perimeter or area followed by a comma and then either the length of the side or the radius.\n")

split_input = user_input.split(",") # remove comma

if split_input[0] == "square": # square
    if split_input[1] == "perimeter":
        print(get_square_perimeter(int(split_input[2])))
    elif split_input[1] == "area":
        print(get_square_area(int(split_input[2])))
    else:
        print(get_cube_volume(int(split_input[2])))
elif split_input[0] == "triangle": # triangle
    if split_input[1] == "perimeter":
        print(get_perimeter_triangle(int(split_input[2])))
    elif split_input[1] == "area":
        print(get_triangle_perimeter(int(split_input[2])))
    else:
        print(get_tetrahedron_volume(int(split_input[2])))
else:
    if split_input[1] == "perimeter": # circle
        print(get_circle_perimeter(int(split_input[2])))
    elif split_input[1] == "area":
        print(get_circle_area(int(split_input[2])))
    else:
        print(get_sphere_volume(int(split_input[2])))

# test assertions
'''
input = circle,perimeter,8
output = 50.26548245743669

input = triangle,volume,9
output = 171.82694782833107
'''

'''
For Challenge 11, we can use the Mediator Method pattern to carry out the
different functions that work out perimeter, volume and area. The mediator
class can be the class that receives the user input for which calculation they
would like to explore and what shape they would like. Then you could have
classes of each shape that have the calculations as seen above. Therefore the
mediator class would be the class that shares the input with these calculations
in order to find out the perimeter, area or volume of the different shapes.
'''
