# LA50_SearchingStrings.py
# @ author: Administrator
# Date: 1.11.23

# stored string
stored_string = "The first rule of fight club is: do not talk about fight club."

# Challenge 1 - counting spaces using count()
print("The number of times that a space appears in this string is {0}\n".
      format(stored_string.count(" ")))

# output
# The number of times that a space appears in this string is 12

# Challenge 2 - counting punctuation using count()
print("The number of times that a punctuation appears in this string is: \n", 
      (stored_string.count(":") + stored_string.count(".")))

# output
# The number of times that a punctuation appears in this string is: 2


# Challenge 3 - checking first word with startswith()
user_input = input("Please type a case sensitive sentence...\n")

print("Does the sentence you typed start with the same first word as the stored string? {0} \n"
      .format(user_input.startswith(user_input)))

# output
# Please type a case sensitive sentence...The dog jumped
# Does the sentence you typed start with the same first word as the stored string? True 


# Challenge 9 - creating a password
password = input("Please type a password: \n")
contains_numbers = False
contains_uppercase = False

# needs to match the follow rules
if len(password) < 8:
    print("The password must contain at least 8 characters")
if any(c.isalpha() for c in password) == False:
    print("The password must contain at least one alphabetical character")
if any(c.isdigit() for c in password) == False:
    print("The password needs to contain at least one number")
if any(c.isupper() for c in password) == False:
    print("The password needs to contain at least one uppercase character")

# input
# Please type a password: 
# apassword
# output
# The password needs to contain at least one number
# The password needs to contain at least one uppercase character

# input
# Please type a password: 
# Password123


# Challenge 10 - creating a new list
list_1 = ["tyler.durden@gmail.com", "marla.singer@hotmail.co.nz"]
list_2 = []

for i in range(0, len(list_1)):
    dot_index = list_1[i].find(".")
    at_index = list_1[i].find("@")

    first_name = list_1[i][0:dot_index] # grabbing the first name
    last_name = list_1[i][dot_index + 1:at_index] # grabbing the last name

    title_first_name = first_name.title() # capital letter
    title_last_name = last_name.title() # capital letter

    list_3 = []
    list_3.append(title_first_name) # appending to new list
    list_3.append(title_last_name) # appending to new list

    list_2.append(list_3)

print(list_2)
# input = ["tyler.durden@gmail.com", "marla.singer@hotmail.co.nz"]
# output = [['Tyler', 'Durden'], ['Marla', 'Singer']]


'''
For Challenge 10, the Mediator Method pattern could be used to create new lists
or instances by separating email addresses as seen above. The mediator class
would contain the calculations above and the email classes would create
instances that interact with each other in order to use the for loop above.
The main method would contain the user emails that you would like to convert
into a first and last name list.
'''





    


