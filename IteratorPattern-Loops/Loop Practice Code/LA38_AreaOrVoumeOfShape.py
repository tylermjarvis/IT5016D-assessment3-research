# LA38_AreaOrVoumeOfShape.py
# @ author: Administrator
# Date: 25.10.23

# Welcome Message
print("Welcome to the shape calculator\n")

# Variables that start the while loop
chosen_option_valid = False
x_inside_range = False
y_inside_range = False
chosen_option = str
x = int
y = int

# Option Loop - picking surface or volume
while chosen_option_valid == False:
    choice = input("Please choose between the Surface or Volume to carry out the calculation of the surface or the volume\n")

    if choice.lower() == "surface": # to lower prevents conditional being false due to capitalisation
        chosen_option = "surface"
        chosen_option_valid = True
    elif choice.lower() == "volume":
        chosen_option = "volume"
        chosen_option_valid = True
    else:
        print("That is not one of the options, please enter your choice again...\n") 

# Valid X - check if x is valid
while x_inside_range == False:
    x = int(input("Please choose the number for side x\n"))
    if x >= 10 and x > 0:
        print("That length is outside of the range\n")
    else:
        x_inside_range = True

# Valid Y - check if y is valid
while y_inside_range == False:
    y = int(input("Please choose the number for side y\n"))
    if y >= 10 and y > 0:
        print("That length is outside of the range\n")
    else:
        y_inside_range = True

# Calculation for Area
if chosen_option == "surface":
    surface = (10 * 8 - x * y) * 2
    + (3 * 10 * 2) + (3 * 8 * 2) + (y * 3 * 2)
    print("The surface area of this shape is: ", surface, "\n")


# Calculation for Volume
if chosen_option == "volume":
    volume = (10 * 3 * (8 - y))
    + (y * 3 * (10 - x))
    print("The volume of this shape is: ", volume, "\n")       


# assertion test case 1
# chosen_option = surface
# x = 8
# y = 3
# output = 112
 
# assertion test case 2
# chosen_option = volume
# x = 10
# y = 4
# output = 120

'''
Iterators can be used within while loops, however in this example an iterator is not
needed, as the while loop is only carried out to select the surface and volume
of a shape. If an iterator was to be used in a while loop, it would commonly
loop through numbers sequentially until it reaches the max number within the
range.
It is important to note that using an iterator in a while loop, allows you
to follow the Single Responsibility Principle and separate your collection
search from the collection that you are searching, therefore you don't have the
collection holding the collection of data and searching that data. An Iterator
function is the best option for tidy and efficient code.
'''
