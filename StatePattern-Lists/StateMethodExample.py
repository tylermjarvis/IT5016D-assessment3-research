# StateMethodExample.py
# @ author: Administrator
# Date: 22.11.23


# State class: Base State class
class State:
    # Base state. This is to share functionality
    def scan(self):
        # Scan the dial to the next station
        self.pos += 1
 
        # check for the last station
        if self.pos == len(self.stations):
            self.pos = 0
        print("Visiting... Station is {} {}".format(self.stations[self.pos], self.name))
 
# Separate Class for AM state of the radio
class AmState(State):
 
    # constructor for AM state class
    def __init__(self, radio):   
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"
 
    # method for toggling the state
    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate
 
# Separate class for FM state
class FmState(State):
    # constructor for FM state
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"
 
    # method for toggling the state
    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate
 
# Dedicated class Radio
class Radio:
    # A radio. It has a scan button, and an AM / FM toggle switch.
    def __init__(self):
        # We have an AM state and an FM state
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate
 
    # method to toggle the switch
    def toggle_amfm(self):
        self.state.toggle_amfm()
 
    # method to scan
    def scan(self):
        self.state.scan()
 
# main method
if __name__ == "__main__":
    # create radio object
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2
 
    for action in actions:
        action()

# Expected Output
'''
Visiting... Station is 89.1 FM
Visiting... Station is 103.9 FM
Visiting... Station is 81.3 FM
Switching to AM
Visiting... Station is 1380 AM
Visiting... Station is 1510 AM
Visiting... Station is 1250 AM
Visiting... Station is 1380 AM
Visiting... Station is 1510 AM
Visiting... Station is 1250 AM
Switching to FM
Visiting... Station is 89.1 FM
Visiting... Station is 103.9 FM
Visiting... Station is 81.3 FM
'''

'''
In the above example we are creating a solution for a radio which has two states
Am State and Fm State. The radio's state will change as we use the toggle button
to listen to different stations. Using the State Method pattern we can use
classes for each state of the radio object and put all state specfic behaviours
into these state classes. We can store the station frequencies in a list object
named stations within each state class and then access this list within the
State class that controls the behaviour of the state classes with a method
called scan. Upon searching for the last station, we can calculate the length
of each list and assign it to the pos (dial position) variable to then access
the last stations index within the station's list.
This example shows us a pratical and real life scenario for using the list
syntax in Python, specifically within the State Method design pattern.

We can also introduce new states without changing the original code of the
current states, therefore this follows the Open/Close Principle. We also
follow the Single Responsibility Principle, as we can organise each state
into separate classes.

This helps us deal with scenarios where we want to change the behaviour of an
object that allows for a new change between different classes. Objects that
may be turned on and off or a car that might have different speeds during a
race. We may also want to cycle through a list that contains different states.
Anything that causes the behaviour to jump around, can be seen as a
stateful object and therefore use the State Method Pattern.

This block of code has inspired me due to it's use of a real life scenario of
an object that has different states. It helps contextualise how you would go
about interacting with an object that has it's behaviour changed multiple times.
It breaks down the problem using simple to follow State classes of AM and FM,
as well as one overall class to control the State.
'''

