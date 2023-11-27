# ReplacingPartOfAString.py
# @ author: Administrator
# Date: 1.11.23

string_1 = "Hello World"
 
# replacing part of a string
print("Replacing part of a string...\n{0}"
      .format(string_1.replace("Hello", "Goodbye")),
      "\n")
 
#Changing Upper and Lower Case Strings
string_1 = "hElLo wOrlD"
print("Making a string upper case...\n{0}"
      .format(string_1.upper()),
      "\n")
 
print("Making a string lower case...\n{0}"
      .format(string_1.lower()),
      "\n")
 
print("Making a string title case...\n{0}"
      .format(string_1.title()),
      "\n")
 
print("Making a string capitalised...\n{0}"
      .format(string_1.capitalize()),
      "\n")
 
print("Making a string swap case...\n{0}"
      .format(string_1.swapcase()),
      "\n")
 
print("Reversing and inserting characters to a string...\n{0}"
      .format("*".join(reversed(string_1))),
      "\n")

'''
String casing can be used through numerous Python design patterns. For the
mediator design pattern, you could include this in the mediator class to change
the desired outcome of all instances communicating with that class.
'''
