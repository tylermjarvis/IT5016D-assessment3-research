# Function4.py
# @ author: Administrator
# Date: 31.10.23

# give score an initial value
score = 4

# function that will increment the score value
def show_new_score():
    score = 4
    score += 1
    print("You got another point...\n"
          "Your score is now {0}.\n"
          .format(score))
    
# input to store score value
x = input("Your score is {0} points...\n\n"
          "Hit any key to get another point. "
          .format(score))

# invoking the function
show_new_score()

# test case assertion
print("Test case assertion: the inital score is 4 "
    "and it should become 5!!")

# show new score
show_new_score()
 
'''
Your score is 4 points...
 
Hit any key to get another point. 

Test case assertion: the inital score is 4 and it should become 5!!
'''

'''
In the example above we can see that these exercises are a good way to approach
large coding problems, as the function utilises the Single Responsibility
Principle. The show_new_score is only in charge of incrementing the score,
therefore if we use the idea that a function only needs to be responsible
for one activity, we can achieve more efficient programs that are easy to
debug and navigate.
'''
