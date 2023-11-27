# RemovingContentFromAString.py
# @ author: Administrator
# Date: 1.11.23

# Python strings have the strip(), lstrip(), rstrip() methods
# for removing any character from both ends of a string.
# If the characters to be removed are not specified then
# white-space will be removed.
 
string_1 = "Hello World"
# Strip off newline characters from end of string_1
string_1.strip("\n")
 
# strip()     removes from both ends
# lstrip()    removes leading characters (Left-strip)
# rstrip()    removes trailing characters (Right-strip)
 
string_1 = "    xyz    "
 
# showing string strip
print("Original string is.... \n")
print("***",string_1,"***\n")
print("Using strip()...\n")
print("***",string_1.strip(),"***\n")
print("Using lstrip()...\n")
print("***",string_1.lstrip(),"***\n")

'''
output
Original string is.... 

***     xyz     ***

Using strip()...

*** xyz ***

Using lstrip()...

*** xyz     ***
'''

'''
Stripping can be used with the Mediator Method pattern to remove parts of the
instances that you do not want. Stripping would be placed within the mediator
class to change the result of the multiple instances.
'''
