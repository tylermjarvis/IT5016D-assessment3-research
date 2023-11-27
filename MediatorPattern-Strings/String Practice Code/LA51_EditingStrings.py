# LA51_EditingStrings.py
# @ author: Administrator
# Date: 1.11.23

# Challenge 1 - create a list of students names in the opposite case

class_size = int(input("Please type your class size\n"))
students = []

for i in range(0, class_size):
    name = input("Please enter a students {0} name\n"
                 .format(i + 1))
    students.append(name)

student_string = ", ".join(students)

print("The names of the students in swapped case are: \n{0}"
      .format(student_string.swapcase())) # swapping the case
                
# test assertion
'''
input class_size = 3
input student name 1 = Tyler
input student name 2 = Matt
input student name 3 = Lisa

output = The names of the students in swapped case are: 
tYLER, mATT, lISA
'''


# Challenge 2 - replaces spaces with -
user_sentence = input("Please type a sentence: \n")

print("Replacing spaces with dashes: \n{0}\n"
      .format(user_sentence.replace(" ", "-")))

# test assertion
'''
input user_sentence = Hello this is a sentence
output = The names of the students in swapped case are: 
Hello-this-is-a-sentence

input user_sentence = My name is Tyler
output = The names of the students in swapped case are: 
My-name-is-Tyler
'''


# Challenge 3 - reverse the string
stored_string = "This is a stored string"

string_length = len(stored_string)

sliced_string = stored_string[string_length::-1]

print (sliced_string)

# test assertion
'''
stored_string = This is a stored string
output = gnirts derots a si sihT
'''


# Challenge 6 - spaces are * and every 5th letter is a capital
sentence = "The only thing that scares me is Keyser Soze."

sentence = sentence.replace(" ","*")
sentence = sentence.lower()

new_sentence = ""

for i in range(0, len(sentence)):
    if i % 5 == 0:
        letter = sentence[i]
        letter = letter.upper()
        new_sentence += letter
    else:
        new_sentence += sentence[i]

print(new_sentence)

# test assertion
'''
sentence = The only thing that scares me is Keyser Soze.
output = The*oNly*tHing*That*ScareS*me*Is*keYser*Soze.
'''

'''
For these challenges, it is possible to use the Mediator Method pattern, but
instead of using lists we can modify the instances. We can have the mediator
class modify instances coming from a class that takes strings. In the main
method we can supply the strings to be changed, therefore creating a system
that is easy to refactor or supply strings to.
'''



