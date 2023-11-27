# LA36_CrapsRoller.py
# @ author: Administrator
# Date: 20.10.23

# Import the random function
import random 

# Craps Roller

# Generate random dice numbers using randomint
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1

total = die1 + die2

# print the result
print("You rolled a", die1, "and a", die2, "for a total of", total)




