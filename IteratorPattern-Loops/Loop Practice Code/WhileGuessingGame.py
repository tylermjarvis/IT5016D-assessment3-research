# WhileGuessingGame.py
# @ author: Administrator
# Date: 25.10.23

import random 

# User Input
print("I'm thinking of a number between 1 and 100.")

# Set the number to be guessed
number = random.randint(1, 100)
user_input = int(input("What is your guess?\n"))
last_guess = int
guesses = 1
found = False

# The game - uses a while loop and a boolean value to initiate the loop
while found != True:
    if user_input > number: # conditionals control the behaviour of the guessing game
        print("Too large!")
        if last_guess != user_input:
            guesses += 1
        last_guess = user_input
        user_input = int(input("What is your guess?\n"))
    elif user_input < number:
        print("Too small!")
        if last_guess != user_input:
            guesses += 1
        last_guess = user_input
        user_input = int(input("What is your guess?\n"))
    else:
        guesses += 1 # This is a form of iteration using increments - giving us data that we could iterate through to find how long it took to guess the number
        print("Nice one! That's the number I was thinking of!! The number was", number, "\n")
        found = True
        
print("It took you", guesses, "guesses to figure out the number")


# assertion test case 1
# number 60
# input guess = 70
# output = Too large!
# input guess = 60
# output = Nice one! That's the number I was thinking of!! The number was 60, It took you 2 guesses to figure out the number
 
# assertion test case 2
# number 25
# input guess = 30
# output = Too large!
# input guess = 30
# output = Too large!
# input guess = 25
# output = Nice one! That's the number I was thinking of!! The number was 25, It took you 2 guesses to figure out the number

'''
Iteration is not used here but could be used after the guessing game to possibly
see how many guesses it has taken the user to guess the number.
'''
