# StringsAndLists3.py
# @ author: Administrator
# Date: 1.11.23

string_1 = "Ka mate kāinga tahi ka ora kāinga rua."

# startswith()
print("Does this string start with Ka?....{0}\n".format(string_1.startswith("Ka")))

# startswith()
print("Does this string start with Tr?....{0}\n".format(string_1.startswith("Tr")))

# endswith()
print("Does this string end with rua?....{0}\n".format(string_1.endswith("rua.")))

# output
'''
Does this string start with Ka?....True
Does this string start with Tr?....False
Does this string end with rua?....True
'''

'''
As seen in the other practice code exercises, we can use the Mediator Method
as an example of how to use string methods to communicate with multiple classes.
String methods like startswith() and endswith() all have uses that the mediator
class may have."
'''

