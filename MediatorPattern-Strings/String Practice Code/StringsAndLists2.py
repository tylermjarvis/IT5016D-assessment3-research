# StringsAndLists2.py
# @ author: Administrator
# Date: 1.11.23

string_1 = "here is a translation: Haera mai ki konei means come here!"

# counting k
print("The number of times that k appears is {0}\n"
      .format(string_1.count("k")))

 # using find() to find a word in the string
konei_endindex = string_1.find("konei") + len("konei")
print("The end index position of konei is {0}\n"
      .format(konei_endindex))

# using find() to find here but after the word konei
here_position = string_1.find("here", konei_endindex, len(string_1))
print("Looking for the string_1 here, anytime after konei...\n\n"
      "The string_1 here appears at index position..{0}"
      .format(here_position))
 
# ouput
'''
The number of times that k appears is 2
The end index position of konei is 41
Looking for the word here, anytime after konei...
The word here appears at index position..53
'''

'''
When looking for specific string data we can use the examples above as one means
to separating data or locating data within a string after a specific word for
example. Again this can be used within the Mediator Method. An example of this
would be using the mediator class to filter out data within the instances of
other classes. We may want to use find to locate specific data to work with.
The Mediator Method is therefore perfect as a one class source for filtering
information from other classes.
'''
