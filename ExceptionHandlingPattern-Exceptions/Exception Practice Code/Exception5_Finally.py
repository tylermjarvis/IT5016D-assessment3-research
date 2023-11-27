# Exception5_Finally.py
# @ author: Administrator
# Date: 2.11.23

# Catching all errors is the best way to program, as it allows for constant
# feedback during the execution of the program
entry_is_valid = False
number_of_goes = 0
while not entry_is_valid:
    try:
        number_entered = int(input("Enter a valid positive integer\n"))
        if number_entered <= 0:
            raise ValueError("Entered value is not a positive integer.")
    except ValueError as e:
        print("The entry is not valid:\n{0}\n"
              "Please try again..."
              .format(e))
    else:
        entry_is_valid = True
        print("Thank you. The acceptable number entered "
              "was {0}.".format(number_entered))
        
    # If you would like a code block to run regardless of the result, you can
    # run the finally code block.
    # The finally code block is usually used as clean up code, that reverts
    # everything back to zero in order to conserve memory
    finally:
        number_of_goes += 1
        print("The number of goes used is...{0}"
              .format(number_of_goes))
 
# Output
'''
Enter a valid positive integer
Four
The entry is not valid:
invalid literal for int() with base 10: 'Four'
Please try again...
The number of goes used is...1
Enter a valid positive integer
-1
The entry is not valid:
Entered value is not a positive integer.
Please try again...
The number of goes used is...2
Enter a valid positive integer
2
Thank you. The acceptable number entered was 2.
The number of goes used is...3
'''

'''
Using the try, except, else and finally process we can direct the program to
all results that could be possible. This is important as we are looking at
the program as a whole (cleaning up with finally, exception handling, etc...)
and not just the good outcomes that we expect. Because a program can take
a variety of inputs, it is important to think about what those imputs can do
to the program you have created. That is why the Exception Error Handling
pattern is necessary, due to the importance of usability and problem solving.
'''
