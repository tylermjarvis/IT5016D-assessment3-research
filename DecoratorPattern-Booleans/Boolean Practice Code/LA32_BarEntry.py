# LA32_BarEntry.py
# @ author: Administrator
# Date: 19.10.23

# date needs to be imported
from datetime import date

# user input is received for the conditional statement
year_of_birth = input("Please enter your year of birth: ")
name = input("Please enter your name: ")

# convert the year to the current year
current_year = (date.today().year)

# Conditional statement
print("\nThe result of your application is",
      str((current_year - int(year_of_birth) >= 21)
      and name != "Suzanne May"
      and name != "Wiremu Rangi"), ".")

'''
This example could use the Decorator Method to add information to a patron
to see if they are eligible to enter the bar.
'''
