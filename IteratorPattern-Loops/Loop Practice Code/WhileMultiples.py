# WhileMultiples.py
# @ author: Administrator
# Date: 25.10.23

password = input("Please type your password\n")
password_attempt = input("Please enter your password... or type Exit\n")
count = 0
correct_password = False

#loop until the user gets the right password or has run out of guesses
while count < 2 and correct_password == False:
    if password == password_attempt:
        print("That is the correct password!\n")
        correct_password = True
    elif password_attempt == "Exit":
        print("You have exited the password page\n")
        correct_password = True
    else:
        print("That is not the correct password... Please try again\n")
        password_attempt = input("Please enter your password\n")
        count += 1
        

# assertion test case 1
# input password
# input attempt = password
# output = That is the correct password!
 
# assertion test case 2
# input password1
# input attempt = password
# output = That is not the correct password... Please try again
# input attempt = password1
# output = That is the correct password!

'''
Because we are not returning data we do not need to iterate through this while
loop.
'''

