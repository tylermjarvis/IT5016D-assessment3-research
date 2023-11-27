# LA49_FunctionPractice.py
# @ author: Administrator
# Date: 31.10.23
 
# Challenge 1

# 1 NZD to 0.55 EUR

# get user input for the conversion
conversion_rate = float(input("Please type the conversion rate between the NZD and the EUR: \n"))

convert = input("Would you like to convert 'to' or 'from' the NZD? \n")

amount = float(input("Please enter the amount you would like to convert: \n"))

# function that calculates converting to or from a currency
def get_convert(conversion_rate, convert, amount):
    result = float
    if convert == "to":
        result = amount * conversion_rate
    else:
        result = amount * (1 / conversion_rate)
    return result

# calling the function and storing it in exchange_rate
exchange_rate = get_convert(conversion_rate, convert, amount)

print("The total amount when converting {1} NZD is {0}\n".format(exchange_rate, convert))

# test assertions
'''
converson_rate input = 0.55
convert input = "to"
amount input = 50000.00
final output = The total amount when converting to NZD is 27500.000000000004

converson_rate input = 0.55
convert input = "from"
amount input = 30000.00
final output = The total amount when converting from NZD is 54545.454545454544
'''


# Challenge 5
# create a list with strings
list_of_words = ["toyota", "nissan", "ford", "holden", "mazda", "kia"]

# create a list that will take string size numbers
list_lengths = []

# function that loops each string character and stores it as a number to
# be appended it to list_length
def word_lengths(list_of_words):
    for i in range(0, len(list_of_words)):
        number = len(list_of_words[i])
        list_lengths.append(number)

# call the function with the list of words as a parameter
word_lengths(list_of_words)
print(list_lengths)


# calculating a different list of words
list_of_words_2 = ["orange", "banana", "apple"]
list_lengths_2 = []

def word_lengths(list_of_words_2):
    for i in range(0, len(list_of_words_2)):
        number = len(list_of_words_2[i])
        list_lengths_2.append(number)

word_lengths(list_of_words_2)
print(list_lengths_2)

# test assertions
'''
list_of_words = ["toyota", "nissan", "ford", "holden", "mazda", "kia"]
list_lengths = [6, 6, 4, 6, 5, 3]

list_of_words = ["orange", "banana", "apple"]
list_lengths = [6, 6, 5]
'''


# Challenge 6
# initialise the starting number to be counted down from
start = 99

part_1 = "bottles of beer on the wall, "
part_2 = "bottles of beer. Take one down, pass it around, "
part_3 = "bottles of beer on the wall."

# a function that decrements the start variable from range 0, start
def get_full_song(start):
    print(start, part_1, part_2, start - 1, part_3)
    start -= 1
    return start

for i in range(0, start):
    start = get_full_song(start)


# test assertions
'''
first output = 99 bottles of beer on the wall,
bottles of beer. Take one down, pass it around,
98 bottles of beer on the wall.

last output = 1 bottles of beer on the wall,
bottles of beer. Take one down, pass it around,
0 bottles of beer on the wall.
'''

