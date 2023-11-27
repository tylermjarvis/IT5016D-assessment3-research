# LA34_NameTheTriangle.py
# @ author: Administrator
# Date: 19.10.23

# Triangle types
# All sides are the same is a equilateral
# All three sides have different lengths is a scalar
# Two sides of the same length is a isoceles

# User input
side_a = int(input("What is the length of the first side: \n"))
side_b = int(input("What is the width of the second side: \n"))
side_c = int(input("What is the height of the third side: \n"))

# Conditional Statement that decides on the triangle
# All sides equal the same
if side_a == side_b == side_c:
    print("The triangle is a equilateral")

# No sides are equal
if side_a != side_b != side_c:
    print("The triangle is a scalar")

# One side is equal with another but not the third side
if side_a == side_b and side_a != side_c \
   or side_a == side_c and side_a != side_b \
   or side_b == side_c and side_b !=side_a:
    print("The triangle is a isoceles")


# Test assertion cases
          
# side_a = 5
# side_b = 5
# side_c = 5
# The triangle is a equilateral

# side_a = 5
# side_a = 7
# side_a = 5
# The triangle is a isoceles

'''
This is a good example for the Decorator Method, as we can use a base code for
the triangle and decorate it differently depending on the different triangles
that the user choses. This would also help with the design principle of
Open/Closing code blocks and Single Responsibility. This is because, once we
have created the base triangle we no longer need to touch this code, due to the
decorators being used to decide how to deal with the different triangle types.
We also have each decorator dealing with only one triangle each.
'''



