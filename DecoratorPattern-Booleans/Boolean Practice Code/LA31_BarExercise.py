# LA31_BarExercise.py
# @ author: Administrator
# Date: 19.10.23

'''
In order to access the date function we need to import it from datetime
'''
from datetime import date

# The program to help the bar manager vet patrons
print("To help the bar manager vet patrons from the bar\n")

# Bar patron should be over 21 years old
print("Bar patron should be over 21 years old\n")
 
# Suzanne May and Wiremu Rangi are not allowed in the bar
print("Suzanne May and Wiremu Rangi are not allowed in the bar\n")

# get data from user
year_of_birth = input("Please enter your year of birth: \n")
user_name = input("Please enter your full name: \n")

# do a calculation - year is converted into a date today
current_year = (date.today().year)

'''
Conditional case - using > we are comparing two statements, therefore leading
to a boolean data type as the result (True or False).
This is useful when comparing multiple values.
We are also using the "and" statement which is important where you need two
conditions to be met, otherwise the next condition in the conditional statement
will run.
'''

print("The result for if the patron can enter the bar is ",
      str((current_year - int(year_of_birth) >= 21)
      and user_name != "Suzanne May"
      and user_name != "Wiremu Rangi"), ".")

# Test assertion cases
# Should be True
# Richard Gear
# 23

# Should be False
# Suzanne May
# 35

'''
Using the conditional Decorator pattern we can include operators that include
two conditions, for example using "and" to make sure that both conditions are
met in order to execute.
'''




