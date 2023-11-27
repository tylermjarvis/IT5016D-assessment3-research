# LA40_ListChallengeTwo.py
# @ author: Administrator
# Date: 26.10.23

list_1 = [ 23, 66, 23, 12 ]
list_2 = [ 1,19, 4, 8 ]
list_3 = [ "land of ", "the ", "the long white cloud" ]

# Challenge 1 - take user input selection of sum or average and return the results
list_sum = (sum(list_1) + sum(list_2))
user_input =input("Please enter either average or sum\n")

if user_input.lower() == "average":
     average = float(list_sum) / (len(list_1) + len(list_2))
     print("The average of list 1 and list 2 is: ", average)

if user_input.lower() == "sum":
     print("The sum of list 1 and list 2 is: ", list_sum)

# sum input = sum
# sum output = 156
# average input = average
# sum average = 19.5

# Challenge 5 - using the length of the list to grab the number of a certain index
for i in range(1, len(list_2), 2):
     print(list_2[i])

# output 19

# Challenge 8 - grabbing 2 random  number in the list
import random

item_1 = (random.choice(list_2))
item_2 = (random.choice(list_2))

while item_1 == item_2:
    item_2 = (random.choice(list_2))

print(item_1, " ", item_2)
 
# output = two random numbers from list_2 Example output 1 = (4, 1) Example output 1 = (19, 8)


# Challenge 9 - reorganising the list of strings
joined_list = "".join(sorted(list_3, key=len))
print(joined_list)

# output = "the land of the long white cloud"

my_list = ['p','r','o','b','e']
print(my_list[0])
print(my_list[2])
print(my_list[-1])

# Expected output "p" "o" "e" - printing based on index

n_list = ["Happy","Car",0.3, [2,0,1,6]]
print(n_list[1:2])
n_list_strings = ["Happy","Car"]
n_list_strings2 = ["Drive"]
print(n_list_strings + n_list_strings2)

# Expected output ["Car"]
# Expected output ["Happy", "Car", "Drive"]

# Days of the week in Maori
maori_week_days = ["Rāhina", "Rātu", "Rāapa", "Rāpare", "Rāmere", "Rāhoroi", "Rātapu"]
print(maori_week_days[1], maori_week_days[6])
print(maori_week_days[-3])

'''
Challenge 9 uses indexes of a list to print desired results. Iterators are used
in a couple of the challenges above, however only one of the challenges requires
an iterator. This challenge offers the list length as a value within the range
to be iterated through. It shows that we can iterate through different areas in
a collection with different list functions. Therefore use what we have learnt
in these examples in an Iterator function to help return desired results from
a collection.
'''

