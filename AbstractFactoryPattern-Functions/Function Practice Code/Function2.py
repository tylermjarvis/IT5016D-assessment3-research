# Function2.py
# @ author: Administrator
# Date: 31.10.23
 
def show_hello(param):
    print("Hello there, the number of times this "
          "function is called is {0}!!!\n\n".format(param))
 
 
# creating and setting a counter
counter = 0
print("Testing my second user defined function...\n\n")

# incrementing the counter when the function is called
counter += 1
# invoking the function
show_hello(counter)
 
counter += 1
# invoking the function again
show_hello(counter)
 
'''
Testing my second user defined function...
Hello there, the number of times this function is called is  1 !!!
Hello there, the number of times this function is called is  2 !!!
'''

'''
In the example above we are supplying the function with parameters, which will
be how we can access the factory class in the main method, within the Abstract
Factory Method.
'''

