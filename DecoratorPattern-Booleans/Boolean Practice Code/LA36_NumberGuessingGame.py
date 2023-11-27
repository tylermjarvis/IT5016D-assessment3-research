# LA36_NumberGuessingGame.py
# @ author: Administrator
# Date: 20.10.23

import random 

# Number Guessing Game

# User Input
print("I'm thinking of a number between 1 and 100.")

# Set the number to be guessed using randint
number = random.randint(1, 100)
user_input = int(input("What is your guess? \n"))
guesses = 1

'''
You can use if statements with a loop if the process is carried out multiple
times and it relies on the condition to be met in order to exit the loop
- if user input is not the number keep repeating the while loop
- let the user know if they are close with an if statement that checks the
value of the guessed number.
'''

# The game
while user_input != number:
    if user_input > number:
        print("Lower!")
    else:
        print("Higher!")

    user_input = int(input("What is your guess? \n"))
    guesses += 1

print("Nice one! That's the number I was thinking of!! The number was", number, "\n")
print("It took you", guesses, "guesses to figure out the number")




