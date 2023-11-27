# LA34_VolumeOfShape.py
# @ author: Administrator
# Date: 19.10.23

# The math function is imported
import math

# User Input
user_choice = input("Would you like to find out the volume or surface area of a shape? \n")

# Deciding on the volume or surface. Surface is selected here
if user_choice.lower() == "surface":
    length = int(input("What is the length of the cylinder? \n"))
    radius = int(input("What is the radius of the cylinder circle? \n"))

# Because the object is circular in shape, math.pi is used for the calculation
    print("The surface area of the cylinder is ",
          2 * math.pi * radius * length
          + 2 * math.pi * radius ** 2
          ,"\n")

# Deciding on the volume or surface. Volume is selected here
if user_choice.lower() == "volume":
    length = int(input("What is the length of the cylinder? \n"))
    radius = int(input("What is the radius of the cylinder circle? \n"))
        
    print("The volume area of the cylinder is ", math.pi * radius ** 2 * length,"\n\n")    
        
if user_choice.lower() != "volume" and user_choice.lower() != "surface":          
    print("You can only enter surface or surface area or volume\n")



# Test assertion cases
          
# surface = length = 8, radius = 2, output = 125.66370614359172     
# volume, length = 10, radius = 4, output = 502.6548245743669 
# shape output = You can only enter the surface or the volume

'''
This is the same as the NameTheTriangle exercise, where you can have a cylinder
as the base code that is decorated by user input for the length and radius.
'''



