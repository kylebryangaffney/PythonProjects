
from abc import ABC, abstractmethod


class Vehicle(ABC):  # Vehicle inherits from ABC to become an abstract class
    def __init__(self, name):
        self.name = name
        self.num_of_wheels = 0
        self.num_of_cylinders = 0
        self.cur_speed = 0

    @abstractmethod
    def describe(self):
        pass

    # Shared logic all vehicles
    def accelerate(self, acceleration_rate):
        self.cur_speed += acceleration_rate * self.num_of_cylinders

    def brake(self, brake_rate):
        self.cur_speed -= brake_rate * self.num_of_wheels

    def drive(self, go):
        if go:
            self.accelerate(2)
        else:
            self.brake(5)


class Motorcycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.num_of_wheels = 2
        self.num_of_cylinders = 2

    # Abstract method for only motorcylces, each other child class would need a different one
    def describe(self):
        print(f"{self.name} is a two wheeled death machine with {self.num_of_wheels} wheels and {self.num_of_cylinders} cylinders.")



# Create a child Motorcycle object
my_bike = Motorcycle("Indian Scout")

# Calls the child's implementation of the abstract method
my_bike.describe()

# Call vehicle regular methods
my_bike.drive(True)   # Accelerates
print(f"Speed after accelerating: {my_bike.cur_speed}")

my_bike.drive(False)    # Brakes
print(f"Speed after braking: {my_bike.cur_speed}")
