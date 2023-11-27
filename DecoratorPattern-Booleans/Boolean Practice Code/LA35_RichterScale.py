# RichterScale.py
# @ author: Administrator
# Date: 20.10.23

# Magnitude Descriptor

# User Input
user_input = float(input("What was the magnitude of the earthquake? \n"))

# Using elif statements and the and operation to include a value inbetween
# Here both conditions need to be met in order for the code in that block to run
if user_input >= 10: 
    print("A magnitude ", user_input, "earthquake is considered to be a micro earthquake.\n")

elif user_input >= 8 and user_input < 10: 
    print("A magnitude ", user_input, "earthquake is considered to be a great earthquake.\n")

elif user_input >= 7 and user_input < 8: 
    print("A magnitude ", user_input, "earthquake is considered to be a major earthquake.\n")

elif user_input >= 6 and user_input < 7: 
    print("A magnitude ", user_input, "earthquake is considered to be a strong earthquake.\n")

elif user_input >= 5 and user_input < 6: 
    print("A magnitude ", user_input, "earthquake is considered to be a moderate earthquake.\n")

elif user_input >= 4 and user_input < 5: 
    print("A magnitude ", user_input, "earthquake is considered to be a light earthquake.\n")

elif user_input >= 3 and user_input < 4: 
    print("A magnitude ", user_input, "earthquake is considered to be a minor earthquake.\n")

elif user_input >= 2 and user_input < 3: 
    print("A magnitude ", user_input, "earthquake is considered to be a very minor earthquake.\n")

else:
    print("A magnitude ", user_input, "earthquake is considered to be a meteoric earthquake.\n")

# Test assertion cases
          
# user_input = 5.5 = output = "A magnitude 5.5 earthquake is considered to be a moderate earthquake."    
# user_input = 8.2 = output = "A magnitude 8.2 earthquake is considered to be a great earthquake."    

'''
This example above has taught me how to use if statements to catch a value
within two conditions using the and operator. It has taught me that if
statements have great control over the flow of the code and how we can use if
statements to achieve the same result with the Decorator Method.
'''


