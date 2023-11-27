# GameOver.py
# @ author: Administrator
# Date: 18.10.23
 
print("Program 'Game Over' 2.0")

print("Same", "message", "as before")

print("Just",
      "a bit",
      "bigger")

print("Here", end=" ")
print("it is...")

print(
        """
         _____       ___       ___  ___   _____  
        /  ___|     /   |     /   |/   | |  ___| 
        | |        / /| |    / /|   /| | | |__   
        | |  _    / ___ |   / / |__/ | | |  __|  
        | |_| |  / /  | |  / /       | | | |___  
        \_____/ /_/   |_| /_/        |_| |_____|
         
         _____   _     _   _____   _____   
        /  _  \ | |   / / |  ___| |  _  \  
        | | | | | |  / /  | |__   | |_| |  
        | | | | | | / /   |  __|  |  _  /  
        | |_| | | |/ /    | |___  | | \ \  
        \_____/ |___/     |_____| |_|  \_\

        """
     )

input("\n\nPress the enter key to exit.")


'''
With the Mediator Method pattern, you can have different classes that
instantiate strings. These classes could build an image using a mediator class
that would communicate how they need to work together to create a story, much
like the example above.
This is useful if you want different classes to only hold small bits of
information, but you would like them to create a bigger output.
'''

