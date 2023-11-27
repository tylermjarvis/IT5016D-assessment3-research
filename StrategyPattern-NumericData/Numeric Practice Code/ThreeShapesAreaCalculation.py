# ThreeShapesAreaCalculation.py
# @ author: Administrator
# Date: 18.10.23

# Shape 1
print("Shape 1")

# getting user inputs
j = int(input("Please enter the length of j\n"))
k = int(input("Please enter the length of k\n"))

# working out the 2 parts to get the toal area
total_area = j / 2 * k

print("The area of your shape is ", total_area,"\n")
 
# Testing
print("My assertions are:"
      "\nj = 8, k = 9 output = 36"
      "\nj = 4, 2 = 13 output = 4")

print("")
print("Shape 2")


# Shape 2

# getting user inputs
g = int(input("Please enter the length of g\n"))
s = int(input("Please enter the length of s\n"))
q = int(input("Please enter the length of q\n"))
w = int(input("Please enter the length of w\n"))

# working out the 2 parts to get the total area
total_area = g * s - q * w

print("The area of your shape is ", total_area,"\n")
 
# Testing
print("My assertions are:"
      "\ng = 8, s = 9, q = 5, w = 3  output = 57"
      "\ng = 4, s = 13, q = 7, w = 2 output = 38")

print("")
print("Shape 3")


# Shape 3

# getting user inputs
u = int(input("Please enter the length of u\n"))
m = int(input("Please enter the length of m\n"))
n = int(input("Please enter the length of n\n"))

# working out the 2 parts to get the total area
total_area = m * u + n / 2 * n

print("The area of your shape is ", total_area,"\n")
 
# Testing
print("My assertions are:"
      "\nu = 8, m = 9, n = 5  output = 84.5"
      "\nu = 4, m = 13, n = 7 output = 76.5")

'''
As seen in the examples above, there is a lot of repetition. This could possibly
be refactored into a class that holds shape data and has methods that do
calculations with the shapes. We could then use functions outside of this class
to do specific calculations based on the small changes of each shape. This would
replace the calculations within the class methods.
Therefore following the Single Responsibility Principle.
'''


