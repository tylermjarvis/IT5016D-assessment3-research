# LA34_CellPhoneCharge.py
# @ author: Administrator
# Date: 19.10.23

from decimal import Decimal

# User Input
minutes = int(input("Please state the number of minutes you have used this month: \n"))
texts = int(input("Please state the number of texts you have used this month:\n"))

# Setting up variables
monthly_charge = 1500
additional_minutes_cost = 25
additional_texts_cost = 15
minutes_allowed = 50
texts_allowed = 50
cost_of_extra_minutes = 0
cost_of_extra_texts = 0
call_centre_charge = 44
tax = 0
total = 0

# Conditional Statement
# The /100 allows us to get the monthly_charge in a decimal form
print("Your monthly charge fee is: $", monthly_charge/100,"\n")

# Boolean operation comparing two values with >
if minutes > minutes_allowed:
    cost_of_extra_minutes = (minutes - minutes_allowed) * additional_minutes_cost
    print("Your addtional minutes fee is: ", cost_of_extra_minutes/100 ,"\n")
if texts > texts_allowed:
    cost_of_extra_texts = (texts - texts_allowed) * additional_texts_cost
    print("Your additional texts fee is: ", cost_of_extra_texts/100,"\n")
print("Your 111 call centre fee is: $", call_centre_charge/100,"\n")

# Adding up the final total
subtotal = monthly_charge + cost_of_extra_minutes + cost_of_extra_texts + call_centre_charge
tax = subtotal * 0.05

# Printing the total values
print("Your taxes are: $", round(tax/100, 2),"\n")
print("Your subtotal is: $", subtotal/100,"\n")
print("The total charge is: $", round((subtotal + tax)/100,2),"\n")


# Test assertion cases
          
# minutes = 68, texts = 45, output = additional_minutes_cost = 4.5,
# tax = 1.0,
# total is: $20.94

          
# minutes = 80, texts = 80, output = additional_minutes_cost = 7.5, additional_texts_cost = 4.5
# tax = 1.37,
# total is: $28.81

'''
The example above follows a similar strategy to the previous examples, where
we can have a set mobile plan that changes or becomes decorated with different
deals or uses. This keeps the base mobile plan code functioning as normal,
but wraps it in the different deals that appear and therefore changes its
behaviour on runtime.
By doing this we would be following the Single Responsibility Principle.
'''



