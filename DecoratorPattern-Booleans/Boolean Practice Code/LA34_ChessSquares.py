# LA34_ChessSquares.py
# @ author: Administrator
# Date: 19.10.23

# Setup variables
row = 0

# User input for selected row
row_selected = input("Select the row letter of the square: \n")

# Setup the calculation
if row_selected.lower() == ("a" or "c" or "e" or "g"):
    row = 1

# User input for column
selected_col = int(input("Select the column number of the square: \n"))
square_coordinates = selected_col + row

# Conditional Statement that calculates the module of the number and decides if that is usually a black or white square
if square_coordinates % 2 == 0:
    print("The square is black\n")
else:
    print("The square is white\n")



# Test assertion cases
          
# row selected is 5
# column selected is d
# return = "The square is white"

# row selected is 4
# column selected is h
# return = "The square is black"



