# LA39_Exercise1.py
# @ author: Administrator
# Date: 25.10.23

for i in range(1500, 2701):
    if (i % 7 == 0) and (i % 5 ==0):
        print(i)


'''
An iterator is seen here looping through the range (numbers to loop through)
1500 to 2701. Using conditionals within the loop, we can return mutliples of 5
and 7.
This is a helpful way to use iteration in order to achieve a specific result.
'''
