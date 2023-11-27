# ListPractice.py
# @ author: Administrator
# Date: 26.10.23

L = []
L = ["expression", 1]

L = list() # empty list
# L = list(sequence)

A = B = [] # both names will point to the same list
 
A = []
 
B = A # both names will point to the same list
 
A = []; B = [] # independent lists

len(L) # returns the number of items in the list 
 
# L[i] # returns the item at index i (the first item has index 0)
 
# L[i:j] # returns a new list, containing the objects between i and j.
 
# n = len(L)
 
# item = L[index]

# empty list
my_list = []
# list of integers
my_list = [1, 2, 3]
# list with mixed datatypes
my_list = [1, "Hello", 3.4]
# nested list
my_list = ["mouse", [8, 4, 6]]
 
my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])
# Output: o
print(my_list[2])
# Output: e
print(my_list[-1])
# Error! Only integer can be used for indexing
# my_list[4.0]
# Nested List
n_list = ["Happy", [2,0,1,6]]
# Nested indexing
# Output: a
print(n_list[0][1])
# Output: 5
print(n_list[1][3])
# using negative indexing
# Output: e
print(my_list[-1])
# Output: p
print(my_list[-5])


my_list = ['p','r','o','b','e']
print(my_list[0])
print(my_list[2])
print(my_list[-1])

# Expected output "p" "o" "e"

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

# Expected output Rātu Rātapu
# Expected output Rāmere



