# LA31_BooleanNot.py
# @ author: Administrator
# Date: 18.10.23

# Setup boolean values
is_full_attendance = True
is_mark_below_pass = False
 
# Test case assertion 1: result should be True
print("The student's success status is....\n")
print(is_full_attendance
      and not is_mark_below_pass, "\n")
 
print("Student failed their exam...\n")
is_mark_below_pass = True
 
# Test case assertion 2: result should be False
print("The student's success status is now....\n")
print(is_full_attendance
      and not is_mark_below_pass, "\n")
 
# Output of both tests
'''
The student's success status is....
True 
 
Student failed their exam...
The student's success status is now....
False
'''

'''
Setting variables to True or False can be used for while loops,
where the loop keeps executing based on a variable being True, until a condition
is met and that variable becomes false, therefore exiting that loop.

"and not" is used here as a way of stating that the condition needs to also be
False in order to execute that block of code.

By changing is_mark_below_pass to True we can shape the outcome of this block of
code. Therefore we could use this with the conditional Decorator pattern, in
order to prevent a code block from adding additional features or instructing
it to add additional features (decorating or not decorating).
'''
