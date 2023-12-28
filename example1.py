from abc import ABC, abstractmethod

# Abstract class defining a Vehicle
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Car class inheriting from Vehicle
class Car(Vehicle):
    def start(self):
        return f"{self.name} starting the car engine."

    def stop(self):
        return f"{self.name} stopping the car engine."

# Motorcycle class inheriting from Vehicle
class Motorcycle(Vehicle):
    def start(self):
        return f"{self.name} starting the motorcycle engine."

    def stop(self):
        return f"{self.name} stopping the motorcycle engine."

# Creating instances of Car and Motorcycle
car = Car("Toyota")
motorcycle = Motorcycle("Harley")

# Using polymorphism to start and stop vehicles
print(car.start())  # Polymorphism: Car's start method is called
print(car.stop())   # Polymorphism: Car's stop method is called

print(motorcycle.start())  # Polymorphism: Motorcycle's start method is called
print(motorcycle.stop())   # Polymorphism: Motorcycle's stop method is called
