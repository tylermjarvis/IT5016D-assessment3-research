# IteratorMethodExample.py
# @ author: Administrator
# Date: 23.11.23


# helper method for iterator
def alphabets_upto(letter):
    # Counts by word numbers, up to a maximum of five
    for i in range(65, ord(letter)+1):
            yield chr(i)
 
 
# main method
if __name__ == "__main__":
    alphabets_upto_K = alphabets_upto('K') # goes until K
    alphabets_upto_M = alphabets_upto('M') # goes until M
 
    for alpha in alphabets_upto_K:
        print(alpha, end=" ")
    print()
 
    for alpha in alphabets_upto_M:
        print(alpha, end=" ")


# Iterator Method

# utility function
def inBuilt_Iterator1():
    alphabets = [chr(i) for i in range(65, 91)]
   
    # using in-built iterator
    for alpha in alphabets:
        print(alpha, end = " ")
    print()
 
# utility function
def inBuilt_Iterator2():   
    alphabets = [chr(i) for i in range(97, 123)]
     
    # using in-built iterator
    for alpha in alphabets:
        print(alpha, end = " ")
    print()
 
 
# main method
if __name__ == "__main__" :   
    # call the inbuiltIterators
    inBuilt_Iterator1()
    inBuilt_Iterator2()


'''
The idea behind the Iterator Method is that we are trying to access a data
collection, without using an excessive number of for and while loops.

This helps solve problems seen in the first example, where you want to access
a piece of data in a collection, but you don't want to be repeating the action
over and over. It is also best to follow the Open/Close Principle and
therefore not have the need to access the original code that holds the
collection.

In the first example, we loop until the letter K (one example). In this example
we use an explicitly created Iterator method. This uses a generator (yield) to
generate the data instead of a return. We use i as the iterator in the helper
method to go through a range within the alphabet collection. This is one way
to use the Iterator Method. Here we are assigning the method to new variables
in order to get the data we want to be returned (for example alphabets_upto_K).

The next example is an in-built Iterator Method. We create utility functions to
iterate over a specific range in the collection and add the for loop to that
function. This allows us to call those iterator functions in a clean and
effective way. We therefore only have one block of code that
we can update to change what collection and data we want to find.

It is important to note that by looking at these examples we can see how the
Iterator Method is used to allow us to follow the Principles of Open/Close and
Single Responsibility. We do not need to touch the function or class with the
collection we would like to look through, we only need to reference it and can
therefore make a function that is solely for searching through this collection.
It also shows the clean approach and the most effective way to use an iterator
in a for or while loop. We can see how utility iterator functions and generators
can create ease when working with large data collections that we risk breaking,
if we tried to loop through the collection where it is being stored.

Also seen in the practice code, we can see how there are many different ways to
loop through a collection of data and how we can use things like len() and
indexes to print and yield the information we require.
'''
