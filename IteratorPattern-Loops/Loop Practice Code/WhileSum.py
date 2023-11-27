# WhileSum.py
# @ author: Administrator
# Date: 25.10.23

number = int(input("Please type a number...\n"))
count = 0
total = 0

while count <= number:
    total = total + count
    count += 1

print("number =", number, "sum =", total, "\n")


# assertion test case 1
# input = 25
# output = 325
 
# assertion test case 2
# input = 8
# output = 36

'''
We are using a incrementer to loop until the count is greater or equal to the
user number. Therefore there is iteration happening due to the need to repeat
the process until the desired result.
'''
