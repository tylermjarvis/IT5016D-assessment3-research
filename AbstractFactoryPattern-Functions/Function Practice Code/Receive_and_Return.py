# Receive_and_Return.py
# @ author: Administrator
# Date: 31.10.23
 
# Receive and Return
# Demonstrates parameters and return values
def display(message):
    print(message)

# function returns the number 5    
def give_me_five():
    five = 5
    return five

# function with a while loop that expects y or n
def ask_yes_no(question):
    # Ask a yes or no question.
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
        return response
    
# Output
display("Here's a message for you.\n")
number = give_me_five()
print("Here's what I got from give_me_five():", number)
answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
print("Thanks for entering:", answer)
input("\n\nPress the enter key to exit.")
