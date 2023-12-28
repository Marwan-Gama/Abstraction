from abc import ABC, abstractmethod

# Abstract class defining Animal
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Subclass Dog inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "Running on four legs."

# Subclass Bird inheriting from Animal
class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

    def move(self):
        return "Flying in the sky."

# Creating instances of Dog and Bird
dog = Dog("Buddy")
bird = Bird("Robin")

# Using polymorphism to call methods from different subclasses
print(f"{dog.name} says: {dog.make_sound()}")
print(f"{bird.name} says: {bird.make_sound()}")

print(f"{dog.name} is {dog.move()}")
print(f"{bird.name} is {bird.move()}")
