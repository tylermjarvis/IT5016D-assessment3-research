# LA39_Exercise42.py
# @ author: Administrator
# Date: 25.10.23

# keep entering numbers and then press zero to exit
print("Please type some integers to calculate their sum and average. Please type 0 to exit and see the sum and average.\n")

count = 0
sum = 0.0
number = 1

# continue storing numbers until 0 is entered
while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1

if count == 0:
	print("Please input some numbers\n")
else:
	print("Average and Sum of the above numbers are: ", sum / (count-1), sum)
	
'''
We do not need an iterator here as we are controlling the while loop through
conditionals. The alternative is controlling the user input of numbers with
a range of data, however there is no limit to the numbers that can be entered
in this exercise.
'''
