# LA35_ChineseZodiac.py
# @ author: Administrator
# Date: 20.10.23

# ChineseZodiac

# User Input
user_input = int(input("Please enter the year that you were born: \n"))

'''
Using the % symbol to calculate the remaining value and associate that with a
year
elif is used here as there are different True statements
'''
if user_input % 12 == 0: 
    print("\n", user_input, "is the year of the Monkey\n")

elif user_input % 12 == 1:
    print("\n", user_input, "is the year of the Rooster\n")
    
elif user_input % 12 == 2:
    print("\n" ,user_input, " is the Year of the Dog\n")
    
elif user_input % 12 == 3:
    print("\n" ,user_input, " is the Year of the Pig\n")
    
elif user_input % 12 == 4:
    print("\n" ,year, " is the Year of the Rat\n")
    
elif user_input % 12 == 5:
    print("\n" ,user_input, " is the Year of the Ox\n")
    
elif user_input % 12 == 6:
    print("\n" ,user_input, " is the Year of the Tiger\n")
    
elif user_input % 12 == 7:
    print("\n" ,user_input, " is the Year of the Hare\n")
    
elif user_input % 12 == 8:
    print("\n" ,user_input," is the Year of the Dragon\n")
    
elif user_input % 12 == 9:
    print("\n" ,user_input, " is the Year of the Snake\n")
    
elif user_input % 12 == 10:
    print("\n" ,user_input, " is the Year of the Horse\n")
    
elif user_input % 12 == 11:
    print("\n" ,user_input, " is the Year of the Sheep\n")
    
else:          
    print("I'm sorry that is not a correct year")


# Test assertion cases
          
# user_input = 2004 = output = That is the year of the Monkey."    
# user_input = 1993 = output = That is the year of the Rooster." 

'''
This is quite a large conditional statement and could be refactored to suit
the Single Responsibility Principle. Each if statement could be turned into
their own function that shares data between each of them or a for loop that
loops through each year.
'''


