# LA31_CanEnrol.py
# @ author: Administrator
# Date: 18.10.23

# The program is to work out eligibility a small grammer school in Auckland
print("To work out eligibility for a small grammer school in Auckland\n")

# Student should be under 10-18 years old
print("Student should be 10 to 18 year old\n")
 
# Lives less than 4km from the school
print("Student should live less than 4km from the school\n")
  
# Has the right to stay in NZ
print("Student has the right to stay in NZ\n")

# If student is under 18 but will pay international fees, then they can enroll
print("Student is under 18, but will pay international fees\n")

# Get input from user, plus setting up values for desired output
distance_from_school = float(input('Please enter the distance that you live from the school in Kilometres: '))
age_in_years = int(input('Please enter the students age: '))
has_residency = True
is_paying_international_fees = False

# Conditional case
print("The student's eligibility to enrol is ",
distance_from_school < 4
and age_in_years < 18  
and age_in_years > 10
and has_residency
or age_in_years < 18
and age_in_years > 10
and is_paying_international_fees, "\n")

# Test assertion cases

# Tom
# 3 (kms)
# 12 (years old)
# has_residency = True

# Maria
# 5000 (kms)
# 11 (years old)
# has_residency = False
# is_paying_international_fees = True

'''
This whole exercise could work with the Decorator Method, as we could have a
base block of code that is called enrolment form and everytime a condition
is met, we decorte/update that form with the new information to see if the
student mets the eligibility for the school.
'''



