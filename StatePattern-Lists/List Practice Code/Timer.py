# Timer.py
# @ author: Administrator
# Date: 26.10.23

from datetime import datetime, timedelta

# max duration is 5 seconds
duration = 5
 
run = input("enter s to begin...")
 
period = timedelta(seconds=1)
 
next_time = datetime.now() + period
 
counter = 0
while run == 's' and counter < duration: # start the loop and continue it if duration is less than the counter
    if next_time <= datetime.now():
        print("..", counter)
        counter += 1
        # reevaluate the next_time variable
        next_time += period # this is using the current time plus the previous time to increment
 
'''
enter s to begin...s
.. 0
.. 1
.. 2
.. 3
.. 4
'''
