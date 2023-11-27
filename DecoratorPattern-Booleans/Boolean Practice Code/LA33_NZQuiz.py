# LA33_NZQuiz.py
# @ author: Administrator
# Date: 19.10.23

# date needs to be imported
from datetime import datetime
 
print ("Welcome to the NZ quiz, there are 5 questions to answer")

# Setup variables
score = 0 # This will be incremented each time the user gets a question right
start = datetime.today() # A timer for the quiz
question_one = int(input("How many main islands are there in New Zealand?: \n"))

# Conditional statement to carry out logic based on the answer being right or wrong
if question_one == 3:
    score = score + 1
    print("That is right!\n")
else :
    print("Wrong!\n")

question_two = input("What is the capital of New Zealand?: \n")

if question_two.lower() == "wellington":
    score = score + 1
    print("That is right!\n")
else :
    print("Wrong!\n")

question_three = input("Who are the indigenous people of New Zealand?: \n")

if question_three.lower() == "maori":
    score = score + 1
    print("That is right!\n")
else :
    print("Wrong!\n")

question_four = input("What is the word that refers to New Zealanders, commonly used overseas?: \n")

if question_four.lower() == "kiwi" or "kiwis":
    score = score + 1
    print("That is right!\n")
else :
    print("Wrong!\n")

question_five = input("Who is the New Zealand prime minister?: \n")

if question_five.lower() == "chris luxon":
    score = score + 1
    print("That is right!\n")
else :
    print("Wrong!\n")

# Stored variable may have change depending on the user answering correctly
print("Your score is ", score, "\n")

# Print the timer result - current time - the start time
print("You took this long to complete the quiz ", datetime.today() - start, "\n")


 
# test case assertions
'''
first assertion is:
question 1 - input is 2 = score = 0
question 2 - input is Wellington = score = 1
question 3 - input is Maori = score = 2
question 4 - input is Kiwis = score = 3
question 5 - input is Chris Hipkins = score = 3
final score is 3
'''



