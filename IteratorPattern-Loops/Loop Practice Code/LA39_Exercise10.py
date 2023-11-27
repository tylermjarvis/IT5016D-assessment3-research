# LA39_Exercise10.py
# @ author: Administrator
# Date: 25.10.23

for i in range(0, 50):
    if (i % 15 == 0):
        print("FizzBuzz")
    elif (i % 5 == 0):
        print("Buzz")
    elif (i % 3 == 0):
        print("Fizz")
    else:
        print(i)

'''
The use of the iterator here is important as it shows that the iterator relies
on the order of the conditionals. This is because it sequentially counts through
the data. If FizzBuzz was not the first condition, then it would never print,
due to Buzz and Fizz being multiples of 15 too.
'''
