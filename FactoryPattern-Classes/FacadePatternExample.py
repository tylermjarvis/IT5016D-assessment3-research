# FacadePatternExample.py
# @ author: Administrator
# Date: 21/11/23

# Facade pattern with an example of WashingMachine
class Washing: 
	'''Subsystem # 1'''
	def wash(self): 
		print("I am washing the clothes...") 

class Rinsing: 
	'''Subsystem # 2'''
	def rinse(self): 
		print("I am rinsing the clothes...") 

class Spinning: 
	'''Subsystem # 3'''
	def spin(self): 
		print("I am spinning the clothes...") 

class WashingMachine: 
	# Facade - acting as the face of the tasks, but is not updating any methods
	def __init__(self): 
		self.washing = Washing() 
		self.rinsing = Rinsing() 
		self.spinning = Spinning() 

	def startWashing(self): 
		self.washing.wash() 
		self.rinsing.rinse() 
		self.spinning.spin() 

# main method
if __name__ == "__main__": 

	washingMachine = WashingMachine() 
	washingMachine.startWashing()

'''
The Facade pattern is being used here. The WashingMachine class is the facade,
due to it calling the methods that we require to perform the tasks of a washing
machine, however that is all it is doing.
The classes Washing, Rinsing and Spinning act as Subsystems as part of the
facade. They carry out the methods required to wash the clothes.
This makes it easy to organise your code and split each task and object into
manageable code that only deal with their task. We also only need to call the
WashingMachine class in order to perform all the tasks needed to clean our
clothes. This is an efficient pattern as we can isolate our code into
subsystems that are easy to manage.
It also makes it easier to test each individual code block,
making it better for testing. Just like the Factory Method pattern, we are
using loose coupling, and therefore don't rely on the other classes for each
process, staying true to the Single Responsibility Principle.
Disadvantages are that we may need to change the facade class or method if there
are changes to the subsystem.
The most important aspect of the Facade Method pattern is that we can use it
to divide and break up complex subsystems into a simple interface. If we
encounter a problem that requires a number of tasks which need to be linked.
We can use the facade to link each task and organise them into one main class
with a name that relates to each subsystem.

Refer to the link below for a reference to facade patterns and their uses:
https://www.geeksforgeeks.org/facade-method-python-design-patterns/
'''


