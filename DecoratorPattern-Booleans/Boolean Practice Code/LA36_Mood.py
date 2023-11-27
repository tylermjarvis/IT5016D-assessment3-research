# LA36_Mood.py
# @ author: Administrator
# Date: 20.10.23

import random

print("I sense your energy.  Your true emotions are coming across my screen.")
print("You are...")

# random is used here to meet different conditions and display their block of code randomly
mood = random.randint(1, 3)

if mood == 1:
    # happy
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       -----------
                   """)
elif mood == 2:
    # neutral  
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | ------  |
       |         |
       -----------
                   """)
elif mood == 3:
    # sad
    print( \
    """
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       |  .'.    |
       | '   '   |
       -----------
                   """)
else:
    print("Illegal mood value!  (You must be in a really bad mood).")

print("...today.")




