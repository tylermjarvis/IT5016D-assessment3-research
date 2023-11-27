# LA47_ReturningDataFunctions.py
# @ author: Administrator
# Date: 31.10.23

# Challenge 1
print("Welcome to the short quiz\n")

'''
First attempt
question_1 = int(input("How many wheels does a car have? \n"))
question_2 = input("What colour are the flowers on a pohutukawa? \n")

def quiz_score(score):
    if question_1 == 4:
        score += 1
    else:
        score = 0
'''

# Second attempt
# score variable is set to 0
score = 0

# function that takes the question, answer and score and calculates the users results
def get_quiz_score(question, answer, score):
    print(question, "\n")
    users_guess = input("Answer: ")
    if users_guess == answer:
        score += 1
        print("That is correct!\n")
    else:
        print("Sorry you got it wrong!\n")
    return score

# Question 1
score = get_quiz_score("How many wheels does a car have?\n", "4", 0)

# Question 2
score = get_quiz_score("What colour are the flowers on a pohutukawa?\n", "red", score)

# Printed results
print("Your score for this quiz is: {0}\n\n".format(score))

# test assertions
'''
question_1 = How many wheels does a car have?
users_guess_1 = 4
output = That is correct!
question_2 = What colour are the flowers on a pohutukawa?
users_guess_2 = red
output = That is correct!
final output = Your score for this quiz is: 2

question_1 = How many wheels does a car have?
users_guess_1 = 4
output = That is correct!
question_2 = What colour are the flowers on a pohutukawa?
users_guess_2 = green
output = Sorry you got it wrong!
final output = Your score for this quiz is: 1
'''


# Challenge 2
user_number_1 = int(input("Please type your first number: \n"))
user_number_2 = int(input("Please type your second number: \n"))

# function that takes the sum of both user input numbers
def get_sum_of(number_1, number_2):
    return number_1 + number_2

# print the sum of both numbers using get_sum_of (get is important, due to us returning information in the function)
print("The sum of {0} and {1} is {2}".format(user_number_1, user_number_2, get_sum_of(user_number_1, user_number_2)))

# test assertions
'''
user_number_1 = 3
user_number_2 = 9
output = The sum of 3 and 9 is 12

user_number_1 = 5
user_number_2 = 6
output = The sum of 5 and 6 is 11
'''


# Challenge 3
cost = 0

print("The cost of this parking meter is $4 for the first 2 hours, then $3 for every hour after that.\n")

# function that returns the cost of parking time
def get_parking_cost(hours):
    cost = (hours - 2) * 3 + 4
    return cost

# user input of parking hours
hours = int(input("Please enter your number of parking hours: \n"))
print("The cost of parking for {0} hours is ${1}\n".format(hours, get_parking_cost(hours)))

# test assertions
'''
hours = 8
get_parking_cost = 22
output = The cost of parking for 8 hours is $22

hours = 12
get_parking_cost = 34
output = The cost of parking for 12 hours is $34
'''


# Challenge 7
# function that returns the factorial number
def get_factorial(number):
    counter = 1
    factorial = 1
    while counter <= number:
        factorial *= counter
        counter += 1
    return factorial

# error case that repeats the question if the number is not positive
number = 0
while not int(number) > 0:
    number = input("Please type a positive integer: \n")

print("The factorial of {0} is {1}\n".format(number, get_factorial(int(number))))

# test assertions
'''
number input = 7
get_factorial = 5040
output = The factorial of 7 is 5040

number input = 9
get_factorial = 362880
output = The factorial of 9 is 362880
'''


# Challenge 12
# create a ditionary that holds the item and cost of the item
store = {"Greenstone Koru carving": 265, "Rimu Tiki necklace": 42, "Manaia bone earrings": 311}

# get item quantity
print("Please enter the quantity of each item that you wish to purchase: \n")

# create an empty ditionary for quantity
item_quantity = {}

# function that calculates the quantity of an item with the cost
def get_total_purchase(store):
    subtotal = 0
    for key, value in store.items():
        quantity = input(("{0} @ ${1}, quantity needed?\n".format(key, value)))
        subtotal += int(quantity) * value
    return subtotal

# call the function and store it in the variable subtotal
subtotal = get_total_purchase(store)

print("Subtotal is: ${0} \nGST @ 15% is: ${1} \nGrand Total is: ${2:0.2f}".format(subtotal, .15*subtotal, 1.15*subtotal))

# test assertions
'''
message = Please enter the quantity of each item that you wish to purchase:
Greenstone Koru carving quantity = 2
Rimu Tiki necklace quantity = 3
Manaia bone earrings quantity = 1
Subtotal = $967 
GST @ 15% = $145.04999999999998 
Grand Total = $1112.05

message = Please enter the quantity of each item that you wish to purchase:
Greenstone Koru carving quantity = 1
Rimu Tiki necklace quantity = 1
Manaia bone earrings quantity = 1
Subtotal = $618 
GST @ 15% = $92.7
Grand Total = $710.70
'''

'''
As stated in the Function5 exercise, we may require the need to return a value
from a function. This gives us the ability to create our program following the
Single Responsibility Principle, where we can have functions responsible for
doing a calculation and returning a value. We can then pass this value into
another function to carry out another calculation or activity which it is
solely responsible for.
'''

