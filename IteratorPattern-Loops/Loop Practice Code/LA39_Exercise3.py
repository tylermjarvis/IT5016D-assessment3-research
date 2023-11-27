# LA39_Exercise3.py
# @ author: Administrator
# Date: 25.10.23

import random 

# User Input
print("I'm thinking of a number between 1 and 9.")

# Set the number to be guessed
number, guess_number = random.randint(1, 9), 0

# loop until number is guessed
while number != guess_number:
     guess_number = int(input("What is your guess?\n"))
print("Well guessed!\n")

x = print("Press any key to exit...")

'''
An iterator can be used here, if the number to be guessed was within a specific
range of numbers. We could use i as the iterator to search through the numbers
and exiting the while loop once we have found the guessed number.
'''
