# String5.py
# @ author: Administrator
# Date: 2.11.23

string_1 = "It's only after we've lost everything " \
           "that we're free to do anything"
 
# splitting the string
print("Splitting the string...\n{0}"
      .format(string_1.split()),
      "\n")
 
# splitting the string on the letter e
print("Splitting the string on the letter e...\n{0}"
      .format(string_1.split("e")),
      "\n")
 

Splitting the string...
["It's", 'only', 'after', "we've", 'lost', 'everything', 'that', "we're", 'free', 'to', 'do', 'anything'] 
 
Splitting the string on the letter e...
["It's only aft", 'r w', "'v", ' lost ', 'v', 'rything that w', "'r", ' fr', '', ' to do anything']

'''
Split is the best approach if you are looking for a specific part of a string.
This can be used within the Mediator Method to return parts of strings
to form new strings, such as a password changer that creates a new password with
previous strings. The mediator class could be the class that joins two
password classes and therefore is the communication channel between these two
classes.
'''
