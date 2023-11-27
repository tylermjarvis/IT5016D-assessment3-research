# WhileLoopExercise1.py
# @ author: Administrator
# Date: 25.10.23
 
# set variable
number_of_tries = 3

while True:
    answer = input("What is the meaning of life?...\n")
    if answer == "42":
        print("That is correct!\n")
        break
    else:
        print("That is incorrect, please try again!\n")
        number_of_tries -= 1

    if number_of_tries == 0:
        print("Sorry, you have run out of guesses!")
        break

    print("You have", number_of_tries, "guesses left...\n")
    x = input("Press any key to guess again.\n")


# assertion test case 1
# answer = That is correct!
 
# assertion test case 2
# answers 1,2 then 3 = Sorry, you have run out of guesses!

'''
Due to the use of a boolean value, we do not need an iterator here.
'''
