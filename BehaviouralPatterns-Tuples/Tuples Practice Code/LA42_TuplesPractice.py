# LA42_TuplesPractice.py
# @ author: Administrator
# Date: 26.10.23

# tuple variable
bank_accounts = (("Joe", 33, "234 Great South Road", "022629107"),
                 ("Tama", 6000),
                 ("Suzanne", 21025, "45 Green Lane"),
                 ("Anihera", -75))
 
print("The number of bank accounts is ", len(bank_accounts))
 
# showing names and balances
for i in bank_accounts:
    print("\nThe name is ", i[0], " and the balance is $", i[1])
 
# showing only names with addresses
for i in bank_accounts:
    if len(i)>2:
        print("\nThe name is ", i[0], " and the address is ", i[2])

# Outputs
'''
The number of bank accounts is  4
The name is  Joe  and the balance is $ 33
The name is  Tama  and the balance is $ 6000
The name is  Suzanne  and the balance is $ 21025
The name is  Anihera  and the balance is $ -75
The name is  Joe  and the address is  234 Great South Road
The name is  Suzanne  and the address is  45 Green Lane
'''

# Account is less than 100
low_balance = 100
for i in bank_accounts:
    if i[1] < low_balance:
        print("A customer with less than ${0} is {1}".format(low_balance, i[0]))

# output
# A customer with less than $100 is Joe
# A customer with less than $100 is Anihera

# Only customers with no phone number or no addresses
for i in bank_accounts:
    if len(i) <= 2:
        print("A customer with either no number or address is ", i[0])

# output
# A customer with either no number or address is  Tama
# A customer with either no number or address is  Anihera


# The highest and lowest balances
# Get a list of the balances
balances_list = []
for i in bank_accounts:
    balances_list.append(i[1])
print("The highest balance is ${0}.".format(max(balances_list)))
print("The lowest balance is ${0}.".format(min(balances_list)))
print("The sum of all balances is ${0}.".format(sum(balances_list)))

# output
# The highest balance is $21025.
# The lowest balance is $-75.
# The sum of all balances is $26983.


# All details for all customers
print("The details for all customers is...\n")
for i in bank_accounts:
    print("\n")
    for customer_detail in i:
        print(customer_detail, end=" ")

# output
# Joe 33 234 Great South Road 022629107 
# Tama 6000 
# Suzanne 21025 45 Green Lane 
# Anihera -75

# Only customers with more than $5k or less than $0
print("/nShowing details for customers with more than $5k and less than $0...", end="")
for i in bank_accounts:
    if 0 > i[1] or i[1] > 5000:
        print("\n")
        for customer_detail in i:
            print(customer_detail, end=" ")

# output
# Tama 6000 
# Suzanne 21025 45 Green Lane 
# Anihera -75

'''
Seen in the examples above, we can use a tuple to store strings and integers or
various types of data. We can search through that data as we would with lists
using for loops and if statements. Due to the information containing bank
account details, it is necessary to protect this information, hence the use
of a tuple which is immutable (Cannot have it's information changed). We may
use behavioural patterns to search through the tuple and retrieve data that
we require, but we need to make sure that this data is not overridden during the
behavioural change while using a Python design pattern.

For example we could use the State Method pattern to change the state of an
online bank account. We may have bank account information of a user that we do
not want to change, however we may want to move the program through the bank
statement section of different months. Therefore we can use tuples to hold
all the information needed for the user to access and display each monthly
statement and use the State Method to handle the switch between those months,
while knowing that we cannot change the user's data.
'''
