# InputAndNumbersPractice.py
# @ author: Administrator
# Date: 17.10.23
 
print("If a 2000 pound pregnant hippo gives birth to a 100 pound calf,")
print("but then eats 50 pounds of food, how much does she weigh?")
input("Press the enter key to find out.")
print("2000 - 100 + 50 =", 2000 - 100 + 50) # 2000 pound - 100 pound + 50 pounds

print("\n If an adventurer returns from a successful quest and buys each of")
print("6 companions 3 bottles of ale, how many bottles are purchased?")
input("Press the enter key to find out.")
print("6 * 3 =", 6 * 3) # 6 companions * 3 bottles

print("\n If a restaurant check comes to 19 dollars with tip, and you and")
print("your friends split it evenly 4 ways, how much do you each throw in?")
input("Press the enter key to find out.")
print("19 / 4 =", 19 / 4) # $19 divided by 4 people

print("\n If a group of 4 pirates finds a chest full of 107 gold coins, and")
print("they divide the booty evenly, how many whole coins does each get?")
input("Press the enter key to find out.")
print("107 // 4 =", 107 // 4) # 107 gold coins divided by 4 pirates

print("\n If that same group of 4 pirates evenly divides the chest full")
print("of 107 gold coins, how many coins are left over?")
input("Press the enter key to find out.")
print("107 % 4 =", 107 % 4) # 107 gold coins modulated between 4 pirates

input("\n Press the enter key to exit.")


'''
In the examples above you can use the Strategy Pattern design as a way to
display various mathematical problems which may require specific algorithms
to achieve the desired results. Therefore you want the class with the problems
to display the base code of the problem and then the calculations to be carried
out by functions outside of the class. These functions will replace the methods
in the class, depending on what equation is being calculated.
'''

