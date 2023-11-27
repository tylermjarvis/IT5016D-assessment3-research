class Car:
    # initialise elements of a car
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer / self.time


if __name__ == '__main__':
    # assign the class Car to my_car
    my_car = Car()
    print("I'm a car!")
    
    # wile loop that takes input data to calculate distance driven
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                        "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
            print("Accelerating...")
        elif action == 'B':
            my_car.brake()
            print("Braking...")
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()


'''
This program could be improved with the Exception Handling Method, as we can see
that there are no Python errors or any error handling running in the program.
This is bad for usability and testing, as we are not catering to all potential
outcomes. We have included an if not error handling condition, but the user
may be unsure as to why this error has triggered. Therefore the use of the
Exception Handling Method would best fit within this condition, as it would
supply the user with the information they need. Although by doing this we would
break out of the program. The condition keeps the loop going so that
the user can enter the correct input.
When using error handling, we need to consider everything that error handling
leads to, such as good testing, easier debugging and better usability. However,
there are a number of things to consider with usability, as seen in this
exercise where we do not want to disrupt the while loop. The function is
simple enough that the user will not become lost when they enter an incorrect
input.
'''

