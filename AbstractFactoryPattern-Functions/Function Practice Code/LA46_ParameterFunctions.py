# LA46_ParameterFunctions.py
# @ author: Administrator
# Date: 31.10.23

# Challenge 1
user_name = input("Please type your name: \n")
user_number = input("Please type your phone number: \n")

# function to print username and phone number
def user(name, number):
    print("Hello there, my name is {0} and my number is {1}.\n".format(name, number))

# call the function with the inputs as the parameters
user(user_name, user_number)  

# test case assertion
# input = Tyler and 0211307033
print("Test case assertion: Hello there, my name is Tyler and my number is 0211307033.")
# input = Margret and 0216387934
print("Test case assertion: Hello there, my name is Margret and my number is 0216387934.")


# Challenge 2
selected_number = int(input("Please type a number: \n"))

# function to multiply the user number by 4
def times_four(typed_number):
    counter = 1
    number = typed_number
    while counter <= 4:
        number += selected_number
        counter += 1
        print(number)

# calling the function with the selected number
times_four(selected_number)
print("\n")

# test case assertion
# input = 7
print("Test case assertion: 7, 14, 21, 28, 35")
# input = 4
print("Test case assertion: 4, 8, 12, 16, 20")


# Challenge 6
stored_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("A stored list: ", stored_list, "\n")

# function that prints the amount of even numbers in the list using a for loop
def even_numbers(stored_list):
    counter = 0
    for i, item in enumerate(stored_list):
        if(isinstance(stored_list[i], int)
           and (stored_list[i] % 2) == 0):
            counter += 1
    print("The amount of even numbers in the list is: {0}".format(counter))

# calling the function using the stored list
even_numbers(stored_list)

random_list = [10, 27, 33, 44, 58, 61, 75, 86, 99, 100]
print("A random list of numbers: ", random_list, "\n")

# even_numbers(random_list) Using a random_list to call the even_numbers function

# test case assertion
# stored_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Test case assertion: The amount of even numbers in the list is: 5")
# random_list = [10, 27, 33, 44, 58, 61, 75, 86, 99, 100]
print("Test case assertion: The amount of even numbers in the list is: 5")

'''
There may be cases like in the examples above, where we would like to supply
functions with parameters that can be used throughout the function. This can
be used with a variety of Python Design patterns, if we would like to give a
function data/value from another piece of code in the program.
'''
