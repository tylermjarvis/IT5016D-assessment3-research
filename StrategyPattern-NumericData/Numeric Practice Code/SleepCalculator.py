# SleepCalculator.py
# @ author: Administrator
# Date: 17.10.23
 
print ("Welcome to the Sleep Calculator\n")
user_yob = int(input("Please enter your year of birth...\n"))
days_slept = user_yob * 365
sleep_total = days_slept * 7
 
print("Thank you for your input\n")
print("Your age in years is ", 2023 - user_yob)
print("This is how many hours you have slept ", sleep_total)

'''
In this example we could have a profile system that calculates the sleep of
each user, however it would be best if the profile system is only responsible
for storing profile data and therefore it would be more appropriate to have
a function that replaces the method to calculate sleep time. This would be using
the Strategy Method to cater for the Single Responsibility Principle.
'''

