# AdapterMethodExample.py
# @ author: Administrator
# Date: 21.11.23

# Dog - Cycle
# human - Truck
# car - Car

class MotorCycle:
    # Class for MotorCycle
    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
            return "TwoWheeler"


class Truck:
    # Class for Truck
    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"


class Car:
    # Class for Car
    def __init__(self):
        self.name = "Car"

    def FourWheeler(self):
        return "FourWheeler"

class Adapter:
    """
    Adapts an object by replacing methods.
    Usage:
    motorCycle = MotorCycle()
    motorCycle = Adapter(motorCycle, wheels = motorCycle.TwoWheeler)
    """  
    def __init__(self, obj, **adapted_methods):
            # We set the adapted methods in the object's dict
            self.obj = obj
            self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        # All non-adapted calls are passed to the object
            return getattr(self.obj, attr)

    def original_dict(self):
        # Print original object dict
            return self.obj.__dict__


# main method
if __name__ == "__main__":

    # list to store objects
    objects = []

    # Adapter class adapting to each main class
    motorCycle = MotorCycle()
    objects.append(Adapter(motorCycle, wheels = motorCycle.TwoWheeler))

    truck = Truck()
    objects.append(Adapter(truck, wheels = truck.EightWheeler))

    car = Car()
    objects.append(Adapter(car, wheels = car.FourWheeler))

    for obj in objects:
        print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))


'''
With the Adapter design pattern, we can link classes that would not normally
be linked via the Adapter class. Using this class with an object dictionary
allows us to access their values, such as car and motorCycle and adapt methods
to their object dictionary. Here we update the value of the key named wheels.
This is useful as you may want to add a method to a class object without
updating the class as you want to follow the open/close principle.
Therefore this gives you a way to attach a method to that class with a
is-a relationship to the original class. Because Python works with inheritance,
we can do this.
This is important as it allows us to work with classes that would not be
compatible with each other.
We also use the single responsibility principle by implementing one behaviour
in each method.

An example of where you may want to use the Adapter Method pattern is if you
wanted a class to behave in a similar way to another class that it is
incompatible with, without repeating code. You can attach the adapter method
to it and get it to behave in the same way. For example, you may want a
motorcycle to work like a car.
See example below.
'''

import random

'''
Here we have a class called Car that carries out car functions with methods
relating to a car.
'''
class Car:
    def __init__(self):
        self.generator = random.Random()

    def accelerate(self):
        random_num = self.generator.randint(50, 100)
        speed = random_num
        print(f"The speed of the car is {speed} mph")

    def apply_brakes(self):
        random_num = self.generator.randint(20, 40)
        speed = random_num
        print(f"The speed of the car is {speed} mph after applying the brakes")

    def assign_driver(self, driver_name):
        print(f"{driver_name} is driving the car")


'''
Next we create a adaptee class that would like to collaborate with the Car
class.

Here we have a class called Motorcycle that carries out car functions with
methods relating to a motorcycle.
'''
class Motorcycle:
    def __init__(self):
        self.generator = random.Random()

    # methods are different from the Car class
    def rev_throttle(self):
        random_num = self.generator.randint(50, 100)
        speed = random_num
        print(f"The speed of the motorcycle is {speed} mph")

    def pull_brake_lever(self):
        random_num = self.generator.randint(20, 40)
        speed = random_num
        print(
            f"The speed of the motorcycle is {speed} mph after applying the brakes")

    def assign_rider(self, rider_name):
        print(f"{rider_name} is riding the motorcycle")

'''
Incompatibility Issue:
If we try to invoke the Car class methods with the Motorcycle class we raise an
exception.
We know that when refactoring the original code, we may cause breaks in the
program, therefore it is better to use the Adapter Method pattern.
'''

# Adapter class
class MotorcycleAdapter:

    # We instantiate the motorcyle class as the MotorcycleAdapter
    def __init__(self, motorcycle):
        self.motorcycle = motorcycle

    # We give the adapter class the methods from the Car class
    def accelerate(self):
        self.motorcycle.rev_throttle()

    def apply_brakes(self):
        self.motorcycle.pull_brake_lever()

    def assign_driver(self, name):
        self.motorcycle.assign_rider(name)

car = Car()
bike = Motorcycle()
bike_adapter = MotorcycleAdapter(bike)

# The bike_adapter is then assigned the adapted methods with
# the MotorcycleAdapter class

# Now we can use the same methods of the Car class to make the motorcycle act
# as a car
bike_adapter.assign_driver("Charles")
bike_adapter.accelerate()
bike_adapter.apply_brakes()

'''
This is different to the very first example, as we are creating a new class
with existing methods from another class, as opposed to the first example that
updates the object dictionary with the Adapter Method pattern.
'''
