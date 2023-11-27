# LA44_LoginProgram_1stAttempt.py
# @ author: Administrator
# Date: 27.10.23

# Directory
login_credentials = {
    "username1": "car13",
    "username2": "truck14",
    "username3": "ute15" 
}

print("Welcome to the login page, you have three attempts to login... After three attempts you will be locked out\n")

# create an attempt variable and set it to 0
attempts = 0

# while loop that allows for 3 attempts
while attempts < 3:
    print("Please enter your username and password\n")
    username = input("Username: \n")
    password = input("Password: \n")

    login_successful = False

    # successful login
    for key, value in login_credentials.items():
        if (key == username and value == password):
            login_successful = True
            break
    attempts += 1
    if not login_successful:
        if attempts < 3:
            print("That login is incorrect, please try again...\n")
        else:
            print("I am sorry, you are out of attempts and have been locked out of your account")
            break

# final printed message if login is successful     
if login_successful:
    print("You have successfully logged into your account!")

# Expected output

# test assertions

# test 1
# input username = username2
# input password = truck14
# output = You have successfully logged into your account!

# test 2
# input username = username5
# input password = boat16
# output = That login is incorrect, please try again...
# input username = username4
# input password = plane17
# output = That login is incorrect, please try again...
# input password = boat16
# output = That login is incorrect, please try again...
# input username = username3
# input password = truck14
# output = That login is incorrect, please try again...
# output = I am sorry, you are out of attempts and have been locked out of your account


# Actual Output
'''
Please enter your username and password

Username: 
username1
Password: 
car13
Please enter your username and password

Username:
'''
# Loop continuing after login is a success

