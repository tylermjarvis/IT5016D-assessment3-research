# ThreeShapesAreaCalculationPart3.py
# @ author: Administrator
# Date: 18.10.23

import math

# Shape 1
print("Shape 1")

e = int(input("Please enter the length of e\n"))
d = int(input("Please enter the length of d\n"))

# working out the 2 parts
total_area = d / 2 * math.sqrt(e ** 2 - d ** 2)
print("The area of your shape is ", total_area,"\n")
 
# Testing
print("My assertions are:"
      "\ne = 8, d = 2 output = 7.745966692414834"
      "\ne = 4, d = 3 output = 3.968626966596886")

print("")
print("Shape 2")


# Shape 2

# getting user inputs
f = int(input("Please enter the length of f\n"))

# working out the 2 parts
total_area = f / 2 * f * math.cos(math.radians(40))

print("The area of your shape is ", total_area,"\n")
 
# Testing
print("My assertions are:"
      "\nf = 8  output = 24.513422179807296"
      "\nf = 4 output = 6.128355544951824")

print("")
print("Shape 3")


# Shape 3

# getting user inputs
e = int(input("Please enter the length of e\n"))
g = int(input("Please enter the length of g\n"))

# find the missing length for the triangle
f = g/ math.cos(math.radians(38))

# working out the 2 parts
total_area = f / 2 * g + e * g + (g/2) ** 2 * math.pi/2

print("The area of your shape is ", total_area,"\n")
 
# Testing
print("My assertions are:"
      "\ne = 8, g = 9 output = 155.2038633280361"
      "\ne = 8, g = 13 output = 277.5981839807173")
