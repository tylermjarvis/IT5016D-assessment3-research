# ExceptionHandlingPattern.py
# @ author: Administrator
# Date: 22.11.23

# A class that creates a message when the FileNotFoundError is raised
class FileProcessingError(Exception):
    def __init__(self, message):
        super().__init__(message)

# A code block that checks if the file is found or not
def process_file(file_path):
    try:
        content = read_file(file_path)
        # Process content...

    # Exception with a relevant error message to explain clearly to the user
    except FileNotFoundError as e:
        raise FileProcessingError("Unable to process file.") from e

def read_file(file_path):
    # Simulate a file not found error
    raise FileNotFoundError(f"File not found: {file_path}")

try:
    process_file("example.txt")
except FileProcessingError as e:
    print(f"Error: {e}") # Error: Unable to process file.
    print("Original Exception:", e.__cause__) # Original Exception: File not found: example.txt

'''
Exception Handling is a pattern used to explain clearly to the user of the
program or developer, what is happening during the runtime of the program.
Without error handling, it can be confusing to decipher and debug what is
happening with the program. The Error Handling Pattern can be used within any
program that has an expectation for particular errors. This could be a file not
being found, to an equation that is impossible to calculate, like dividing by
zero. With the exception error message, we can then supply the right information
to the program and receive the desired output.

The example above, explains the importance of displaying a message that is
understandable for the user. This can be achieved through supplying a message
to the FileProcessingError class that is initialising a message.

We can use the Exception Handling pattern as a way to achieve more efficient
code and meet the expectations of the design principles. We can have separate
methods or functions for each exception and build this into our main program,
therefore it is easier to modify, as we are giving one responsibility to each
exception (Single Responsibility Principle). When it comes to debugging it will
be easier to approach due to the development process thinking about all outcomes
and laying out the functions with one responsibility.
'''
