
# letters for encrypting
caesar = [" ", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# message to be encrypted
user_input = input("Please enter in a message that you would like to encrypt, "
                   "followed by a , and the encryption key number: ")

# remove the comma
split_user_input = user_input.split(",")

# put words together
sentence = split_user_input[0]
offset = int(split_user_input[1])

# iterate throughout the characters to produce encrypted word
def get_cipher(sentence, offset):
    result = ""
    for count in range(0, len(sentence)):
        num = ord(sentence[count])
        num += offset
        if num > ord('Z'):
            num -= 26
        elif num < ord('A'):
            num += 26
        letter = chr(num)
        result += letter
    return result

# print encryption
print(get_cipher(sentence, offset))

'''
By using the Exception Handling Method, we can greatly improve this program
for not only debugging purposes but for usability as well. We could throw
an exception with the TypeError error, if the user input is a different type
to a string. To do this we would have to use conditionals or a while
loop that prints an exception of Type Error if the type is not the correct
data type. This helps us cater for user error, and lets the user know what
they need to do next time to correctly run the program. It helps us as
developers to debug and test as we can assume the result of both good and bad
outcomes and therefore prevent mistakes that aren't covered in the program.

In this example we could test the user input for incorrect outcomes. This
would assist us if we were debugging and the input wasn't correct, but the
program continued to run. It would make debugging very frustrating and
time consuming without exception handling.
'''
