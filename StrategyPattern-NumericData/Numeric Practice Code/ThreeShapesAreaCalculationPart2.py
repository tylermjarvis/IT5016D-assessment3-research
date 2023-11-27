# ThreeShapesAreaCalculationPart2.py
# @ author: Administrator
# Date: 18.10.23

# importing math for access to pi
import math

# Shape 1
print("Shape 1")

# getting user inputs
x = int(input("Please enter the length of x\n"))
y = int(input("Please enter the length of y\n"))

# working out the 2 parts
total_area = y * x

print("The area of your shape is ", total_area,"\n")
 
# Testing
print("My assertions are:"
      "\nx = 8, y = 9 output = 72"
      "\nx = 4, y = 13 output = 52")

print("")
print("Shape 2")


# Shape 2

# getting user inputs
c = int(input("Please enter the length of c\n"))

# working out the 2 parts
total_area = c ** 2 * math.pi * 3/4

print("The area of your shape is ", total_area,"\n")
 
# Testing
print("My assertions are:"
      "\nc = 8  output = 150.79644"
      "\nc = 4 output = 37.69911184307752 ")

print("")
print("Shape 3")


# Shape 3

# getting user inputs
e = int(input("Please enter the length of e\n"))
g = int(input("Please enter the length of m\n"))
f = int(input("Please enter the length of f\n"))

# working out the 2 parts
total_area = f / 2 * g + e * g + (g/2) ** 2 * math.pi/2

print("The area of your shape is ", total_area,"\n")
 
# Testing
print("My assertions are:"
      "\ne = 8, g = 9, f = 5  output = 126.30862561759665"
      "\ne = 8, g = 13, f = 7 output = 215.86614480708437")
