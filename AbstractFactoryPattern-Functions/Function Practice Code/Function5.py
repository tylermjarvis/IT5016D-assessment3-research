# Function5.py
# @ author: Administrator
# Date: 31.10.23
 
score = 4
 
def get_new_score(param_score):
    param_score += 1
    print("You got another point...\n"
          "Your score is now {0}.\n"
          .format(param_score))
    return param_score

# input to store score value
x = input("Your score is {0} points...\n\n"
          "Hit any key to get another point. "
          .format(score))

# invoking the function and using it to set the new score
score = get_new_score(score)

# test case assertion
print("Test case assertion: the current score is 5 "
    "and it should become 6!!")
# invoking the function
score = get_new_score(score)
 
'''
Your score is 4 points...
 
Hit any key to get another point. 
You got another point...
Your score is now 5.
 
Test case assertion: the current score is 5 and it should become 6!!
You got another point...
Your score is now 6.
'''

'''
Seen in the example above, we have functions that return a value within a
variable. These functions are refered to as "get" functions and are named in
reference to the fact that they return a value. With the Abstract Factory
Method, we need to use a return function/method in order to receive the values
given by the classes that the factory class will create.
'''
