# LA31_BooleanOr.py
# @ author: Administrator
# Date: 18.10.23

# Setup boolean values
is_fuel_in_tank = True
is_driver_licensed = False
is_driver_insured = True
 
print("This program works out whether you can have a car, or a driver....\n")
 
# Test case assertion 1: result should be True
print("Program output is ",
      is_fuel_in_tank
      or is_driver_licensed
      and is_driver_insured, "\n")
 
print("Removing all the fuel...\n")
is_fuel_in_tank = False
 
# Test case assertion 2: result should be False
print("Program output is now ",
      is_fuel_in_tank
      or is_driver_licensed
      and is_driver_insured, "\n")
 

# Output of both tests
'''
This program works out whether you can have a car, or a driver....
Program output is  True 
 
Removing all the fuel...
Program output is now  False
'''

'''
For this example we could use the Decorator Method to create a dynamic way to
fill the tank with fuel. We could have an empty tank that is the base code,
and this tank is "decorated" with fuel everytime a condition is met.
This could also work the same with the insurance, where we have a policy as the
base code and it is "decorated/renewed" whenever a condition is met.
'''
