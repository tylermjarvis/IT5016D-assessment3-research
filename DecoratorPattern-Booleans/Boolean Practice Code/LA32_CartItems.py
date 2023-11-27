# LA32_CartItems.py
# @ author: Administrator
# Date: 18.10.23

# The program is to direct users as they shop on a website
print("To direct users as they shop on a website\n")

# Shopper is registered
print("Shopper should be registered\n")
 
# The shopping cart contains at least one item
print("The shopping cart contains at least one item\n")
  
# Can make a guest payment
print("Can make a guest payment\n")

# Can purchase gift cards so they do not need an item in their cart
print("Can purchase gift cards so they do not need an item in their cart\n")

# boolean input, will decide on how the following code runs
is_registered = bool(input('Do you have an account with us? '))
item_in_cart = bool(input('Do you have an item in your cart: '))
is_guest = True

# Conditional case
print("You are able to purchase an item on the website if ",
is_registered
and item_in_cart == True
or is_guest
and item_in_cart == False

# Test assertion cases

# Is Registered
# Has an item in their cart

# Is a guest
# Does not have an item in their cart

'''
Input can be used to meet conditions like in this example. This is important
to note when using the Decorator Method as we are not bound by set variables
for conditions to execute.
'''
