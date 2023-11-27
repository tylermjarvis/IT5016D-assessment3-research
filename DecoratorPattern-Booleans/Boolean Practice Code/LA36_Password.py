# LA36_Password.py
# @ author: Administrator
# Date: 20.10.23

print("Welcome to System Security Inc.")
print("-- where security is our middle name\n")

password = input("Enter your password: ")

# A simple if statement that only executes the code if the user input is secret
# Else access the denied block is run
if password == "secret":
    print("Access Granted")

else:
    print("Access Denied")

'''
A security system much like the example above could be used with the Decorator
Method, where the security level is increased each time a decorator function
is added to the base password or security method.You could have the user input
a password and then have the program ask if they would like to add special
characters or more numbers. Therefore adding and changing the behaviour of
the password. Each function is responsible for adding one function to the
password and therefore this allows us to access security of the password without
opening the base code of the password, ticking both the Open/Close Principle
and the Single Responsibility Principle.
'''




