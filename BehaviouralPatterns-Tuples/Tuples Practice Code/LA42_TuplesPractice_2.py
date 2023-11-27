# LA42_TuplesPractice_2.py
# @ author: Administrator
# Date: 26.10.23

# Challenge 1 and 2 - print a tuple
tuple_1 = ("this", "is", "a", "tuple", 1, 2, 3)
print(tuple_1)

# Challenge 3 - print tuple at index 2
tuple_2 = (1, 2, 3, 4, 5)
print(tuple_2[2])

# Challenge 4 - assign tuple index to variables
tuple_3 = ("monkey", "giraffe", "hippo")
monkey = tuple_3[0]
giraffe = tuple_3[1]
hippo = tuple_3[2]

print(monkey, " ", giraffe, " ", hippo, "\n")

# Challenge 5 - lotto balls at tuple index
lotto_balls = (1, 45, 23, 78, 34, 24)
print("The fourth lotto ball was :", lotto_balls[3], "\n")
print("The fourth from last lotto ball was :", lotto_balls[-4], "\n")


# Challenge 6 - display repeated numbers
items = (1, 45, 23, 78, 34, 24, 45, 24, 24)
repeated_items = []
for counter in range (0,len(items)):
    for number in range(counter+1, len(items)):
        if items[counter] == items[number]:
            repeated_items.append(items[number])

individual_repeats = set(repeated_items)
print(individual_repeats)

# Challenge 7 - search for number in tuple and display how many times it was found
items = (1, 45, 23, 78, 34, 24, 45, 24, 24)
found = 0

number = int(input("Enter the value you wish to search for\n"))

for counter in range (0,len(items)):
    if items[counter] == number:
        found += 1

if found == 0:
    print("The number was not in the tuple")
elif found == 1:
    print("The number was in the tuple once")
else:    
    print("The number was in the tuple more than once")

'''
There are many reasons to use tuples, as seen in the examples above. We may want
to display a lotto draw or assign tuple values to variables. We can achieve this
through Python design patterns. However, we do need to think about ways where
the data remains consistent when using different behavioural patterns. Hence the
use of tuples.

Because a tuple works in a similar way to a list, we can use the
behavioural pattern called the Iterator Method. We can use this pattern with
the examples above as Challenge 6 and 7 both have for loops with
iterators (counter). Therefore we can build iterator functions to loop through
the tuples above and yield (generate) the result from the counters. This makes
it easier to cycle through problems like the ones in Challenge 6 and 7, whilst
keeping the data protected, for example, lotto numbers.
'''

