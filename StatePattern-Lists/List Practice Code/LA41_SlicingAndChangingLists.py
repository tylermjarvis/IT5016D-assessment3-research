# LA41_SlicingAndChangingLists.py
# @ author: Administrator
# Date: 26.10.23

# Challenge 1
list_1 = [ 34, 123, 5, 77, 59, 2, 4 ]
print(list_1[2:5]) # print numbers inbetween these indexes

# output = 5, 77, 59


# Challenge 2
list_1 = [ 34, 123, 5, 77, 59, 2, 4, 42, 56, 78, 92, 104]

length = len(list_1)
half = (int(length/2)) # half the list length
print(list_1[0:half]) # using the number returned and assigned to half as the
                      # last index to display

# output = 34, 123, 5, 77, 59, 2

# Challenge 3
list_1 = [ 34, 123, 5, 77, 59, 2, 4, 42, 56, 78, 92, 104]

length = len(list_1)
if length % 4 == 0:
    quarter = (int(length/4)) # get a quarter of the length
    three_quarters = quarter * 3 # times it by 3 for 3/4
    print(list_1[three_quarters: length]) # get the last 3/4 of the list

# output = 78, 92, 104

'''
Just like the exercise, LA41_ListMethods, we can see in these examples that the
index of a list can be accessed in many different ways. This is helpful as we
may want to use the State Method to access the middle of a list
(with index1:index2) within a state class or we may want to get only the
last quarter of the list of states.
'''
