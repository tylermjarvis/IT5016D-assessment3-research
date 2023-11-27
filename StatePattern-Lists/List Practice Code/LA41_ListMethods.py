# LA41_ListMethods.py
# @ author: Administrator
# Date: 26.10.23

# Challenge 1
# Length of List
new_list =[]
list_length = 3                                            
 
for i in range(list_length):
    item = input("Please choose a whole number: \n")
    new_list.append(item) # adding user number to the empty list, new_list
 
print("The new list is: ", new_list)   

# input_1 = 7
# input_2 = 9
# input_3 = 2
# output = 7, 9, 2


# Challenge 3
import random

random_list = []
list_length = 5 
for i in range(list_length):
    item = random.randint(0, 11) # using randomint to randomly select a number between 0, 11
    random_list.append(item) # adding that random number to random_list
 
print("The new list is: ", random_list)

# output = [3, 8, 9, 4, 0]


# Challenge 4
shopping_cart = ["iPhone 7", "MacBook Air", "Surface Tablet"]

user_input = int(input("To remove an item please type one of the following, \n 0 will remove the iPhone 7 \n 1 will remove the MacBook Air \n 2 will remove the Surface Tablet\n"))
if user_input == 0:
    shopping_cart.pop(0) # using pop to remove item at chosen index
elif user_input == 1:
    shopping_cart.pop(1)
else:
    shopping_cart.pop(2)
print(shopping_cart) # new list without removed item

# input = 0
# output = ['MacBook Air', 'Surface Tablet']
# input = 2
# output = ['iPhone 7', 'MacBook Air']

# Challenge 12
import time
random_list = []
seconds = 0
end = 6 # this is the end variable for the while loop
timer = True # this allows the while loop to continue looping

while(timer):
    random_number = random.randint(0, 20)
    random_list.append(random_number)
    time.sleep(1) # each second adds a new number
    seconds += 1 # increment seconds so that we can go to the next random number
    if(seconds >= end):
        timer = False
print("The new list is: ", random_list)

# output after 6 seconds = The new list is:  [9, 0, 16, 0, 3, 10]

'''
With list methods (append, pop) seen in Challenges 1, 3, 4, we can manipulate
the list that we are searching through, by giving it more or less values.
This is an important feature when using the State Method pattern with lists.
This is because we can add or remove values within states during runtime and
therefore change the outcome. By using list methods like those above, we do not
have to refactor our code as we can use other methods or functions to deal with
the list methods and therefore follow the two principles, Open/Close Principle
and Single Responsibility Principle.
'''





