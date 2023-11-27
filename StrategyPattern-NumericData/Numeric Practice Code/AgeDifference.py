# AgeDifference.py
# @ author: Administrator
# Date: 17.10.23
 
from datetime import datetime
from datetime import timedelta
 
date_input = input("Please enter the first persons DOB in the format DD Mmm YYYY: \n")

date_input2 = input("Please enter the second persons DOB in the format DD Mmm YYYY: \n")

# cast to a datetime object
date_object = datetime.strptime(date_input, '%d %b %Y')
date_object2 = datetime.strptime(date_input2, '%d %b %Y')

# do a calculation - minus users DOB from the current date
my_age = datetime.today() - date_object
my_age2 = datetime.today() - date_object2

my_age_years = int(my_age.days/365)
my_age_years2 = int(my_age2.days/365)


# minus 125 days
print("the age difference is ", my_age_years - my_age_years2, ".\n")

'''
Using this code with the Strategy Method Pattern, we could setup a class that
is setting up a user profile. One of the calculations within the profile could
be to figure out the age difference between profiles. Therefore we would have
a class that deals with the profile and have an algorithm within a function,
much like the example above, that can replace a method within the profile class
that presents the age difference of multiple profiles.
'''

