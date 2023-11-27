# LA35_Alphabet.py
# @ author: Administrator
# Date: 20.10.23

# Letter Selector

# User Input
user_input = input("Select a letter from the Alphabet: \n")

'''
It is important to note that edge cases should be used here. For example if
the user types a capital A, the if statement needs to be able to recognise
the input to be True, hence why the lower() is used. This changes the input
to lowercase for the if statement check.
'''
if user_input.lower() == ("a" or "e" or "i" or "o" or "u"): 
    print("The letter", user_input, "is a vowel.\n")

'''
The order is important here as y is a consonant too, so it needs to go before
the else statement which does the remaining function
'''
elif user_input.lower() == "y": 
    print("Sometimes y is a vowel, and sometimes y is a consonant.\n")

else:
    print("The letter", user_input, "is a consonant.\n")

# Test assertion cases
          
# user_input = a = output = The letter a is a vowel."    
# user_input = t = output = The letter t is a consonant."

'''
Seen in this example, you may want to use the Decorator Method to change the
desired outcome. Therefore using the base code of the alphabet, you can decide
whether the decorator functions will handle user input to change the behaviour
and outcome. Each function is responsible for the desired outcome. Therefore
the Single Responsibility Principle is followed.
'''
