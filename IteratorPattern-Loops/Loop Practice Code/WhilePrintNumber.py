# WhilePrintNumber.py
# @ author: Administrator
# Date: 25.10.23

number = int(input("Please type a number...\n"))
count = 0

while count < number:
    print("[", count + 1, "] ", end="")
    count += 1


# assertion test case 1
# input = 6
# output = [1][2][3][4][5][6]
 
# assertion test case 2
# input = 2
# output = [1][2]

'''
Here we are iterating in the form of an incrementer which sequentially prints
the numbers that we are looping through.
'''
