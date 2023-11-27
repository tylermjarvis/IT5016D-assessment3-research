# Concatenation.py
# @ author: Administrator
# Date: 1.11.23

# To concatenate strings in Python use the "+" operator.
# "Hello " + "World" = "Hello World"
# "Hello " + "World" + "!" = "Hello World!"
 
string_1 = "Hello World"

# join string_1 using :
print("Using the join method to add a : between every char...\n{0}"
      .format(":".join(string_1)),
      "\n")

 # join string_1 using  a space
print("Using the join method to add a whitespace between every char...\n{0}"
      .format(" ".join(string_1)),
      "\n")

'''
output
Using the join method to add a : between every char...
H:e:l:l:o: :W:o:r:l:d 

Using the join method to add a whitespace between every char...
H e l l o   W o r l d
'''

'''
We can use the Mediator Method pattern that has a class in charge of different
strings/messages and then use a mediator class to change the output of all of
those messages.
Therefore the mediator class is responsible for changing the different string
classes and the string classes are responsible for supplying their
strings/messages.
'''
