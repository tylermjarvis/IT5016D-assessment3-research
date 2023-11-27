# StrategyMethodExample.py
# @ author: Administrator
# Date: 23.11.23

# A separate class for Item
class Item:
    # Constructor function with price and discount
    def __init__(self, price, discount_strategy = None):
         
        # take price and discount strategy      
        self.price = price
        self.discount_strategy = discount_strategy
         
    # A separate function for price after discount 
    def price_after_discount(self):   
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
             
        return self.price - discount
 
    def __repr__(self):  
        statement = "Price: {}, price after discount: {}"
        return statement.format(self.price, self.price_after_discount())
 
# function dedicated to On Sale Discount
def on_sale_discount(order):    
    return order.price * 0.25 + 20
 
# function dedicated to 20 % discount
def twenty_percent_discount(order):   
    return order.price * 0.20
 
# main function
if __name__ == "__main__":
    print(Item(20000))
     
    # with discount strategy as 20 % discount
    print(Item(20000, discount_strategy = twenty_percent_discount))
 
    # with discount strategy as On Sale Discount
    print(Item(20000, discount_strategy = on_sale_discount))

# Output
'''
Price: 20000, price after discount: 20000
Price: 20000, price after discount: 16000.0
Price: 20000, price after discount: 14980.0
'''

'''
The Strategy Method pattern is used in the example above as a way to add more
than one discount to the shop, as there was previously only one discount.
Therefore using the strategy method we can create a specific class that takes
all the algorithms and puts them in to separate classes, creating a Strategy.
The main class will reference these strategy classes.

Seen in the example, we initialise the price and discount, then we put them
in their own method called price_after_discount. We then take the price and
discount and put them into a strategy. Now we can create the discount functions
that deal with all the different functions of the discount. Within these
functions we have numeric data in the form of integers, carrying out the
discount calculations. Because we have created a discount strategy, we can
now call the discount functions as the discount strategy. In the
price_after_discount method, we are referring to these functions and can
therefore use the data in the function, to calculate the discount.

Because of this strategy, we are isolating the discount code to it's own
function that can be referenced through this method in the Item class.
Therefore, each discount has a single responsibility following the Single
Responsibility Principle.

Because the practice code consists of numeric data, this is a common pattern
that could work well with this strategy, due to the need to do repeated
calculations that arise in every day life, such as a discount or shape
calculation.
'''


