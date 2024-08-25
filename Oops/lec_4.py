# Inheritance in Python is a concept where one class takes on the properties and behaviors (methods and attributes) of another class (called the parent or base class).
# This allows the child class to reuse code from the parent class, and also to extend or modify it as needed
# Example:-

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Bark"  # Overriding the parent method

dog = Dog()
print(dog.speak())

#Single Level Inheritance occurs when a child class inherits from a single parent class.
# This is the simplest form of inheritance, where the child class directly inherits the properties and methods of the parent class.

class Car:
  @staticmethod
  def start():
    print("Car is started")
  @staticmethod
  def stop():
    print("Car is stoped")

class Toyota(Car):
  def __init__(self, name):
    self.name = name
car1 = Toyota("Fortuner")
print(car1.name)

car2 = Toyota("Prius")
print(car2.name)
car1.start()
car2.stop()


