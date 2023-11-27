# LA39_Exercise31.py
# @ author: Administrator
# Date: 25.10.23

# Get Human Years
human_years = int(input("Write your dog's age in human years: \n"))

# Do calculation to convert human years into dog years
if human_years < 0:
    print("That is not a possible age!\n")
    human_years = int(input("Write your dog's age in human years: \n"))
elif human_years <= 2: # dog years are faster when a dog is younger
    dog_years = human_years * 10.5
else:
    dog_years = 21 + (human_years - 2) * 4

print("The dog's age in dog's years is", dog_years)

# assertion test case 1
# human_years = 13
# output = 65
 
# assertion test case 2
# human_years = 3
# output = 25

'''
We do not need to iterate over this, as there is no looping involved.
We would need an iterator if there was a collection of dogs with a variety of
ages.
'''
