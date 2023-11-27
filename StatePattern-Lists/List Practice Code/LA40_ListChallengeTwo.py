# LA4_0ListChallengeTwo.py
# @ author: Administrator
# Date: 26.10.23

# creating a list variable with characters
my_list = ['p','r','o','b','e']
print(my_list[0])
print(my_list[2])
print(my_list[-1])

# Expected output "p" "o" "e"

# accessing indexs of a string to add with another string
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
print(maori_week_days[-3]) # using - will count backwards from the end of the list

# Expected output Rātu Rātapu
# Expected output Rāmere


'''
In these examples we are navigating the values in a list using an index, for
example: my_list[1]. With the State Method, we can use lists to carry out the
same search in order to change the state, however in the GeeksforGeeks example,
we are using the scan method to be the index that moves through the list.
For reference, that is the self.pos variable in the StateMethodExample.py,
that uses an incrementer to move through the list.
From the examples above, we can get an understanding of how an index works and
why it is possible to change the state using an index.
In exercise number one we use my_list[0] to access the "p" value.
'''




