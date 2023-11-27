# LA33_ParkingMeter.py
# @ author: Administrator
# Date: 19.10.23
 
print ("Kia Ora, this is a parking meter")
# park_time = 4
# print ("park_time time is ", park_time, " hours.")

# user input in the form of an int which will be controlled in the conditional statement
user_hours = int(input("how many hours would you like to park for: "))

# pre set values
rate = 4
cost = 0
if user_hours > 3:
    cost = rate *3 
    # drop the rate by $2
    rate -= 2
    # get the remainder of the parking time
    user_hours -= 2
    # print("The user_hours of the parking is ", user_hours)
    # add to the current cost
    cost += rate * user_hours
    print("The cost of the parking is $", cost)
else:
    cost = rate * user_hours
    print ("The cost of the parking is $", cost)


 
# test case assertion 1
'''
user_hours = 10
total cost of parking = $28
'''
'''
user_hours = 8
total cost of parking = $24
'''

'''
One way to use this example with the Decorator Method, is if the price for
parking was to change on a particular day, we can then decorate the parking
function with specific days that parking costs a different amount.
'''



