# Polymorphism in Python allows objects of different classes to be treated as objects of a common parent class.
# It means that the same function or method can operate on different types of objects.
# This ability to use a single interface for multiple forms (types) is known as polymorphism.
from Oops.lec_7 import Example

# Example:-
class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

def animal_sound(animal):
    return animal.speak()

dog=Dog()
cat=Cat()
print(animal_sound(dog))
print(animal_sound(cat))

# Explanation:
# We have two classes, Dog and Cat, both with a method speak(). The method has different implementations in each class.
# The function animal_sound() accepts an object as a parameter and calls the speak() method on that object, without caring if the object is a Dog or a Cat.
# This is polymorphism in action: the same function (animal_sound) can work with objects of different classes (Dog and Cat) because they share a common interface (speak() method).

# @property: A property is a special kind of method that acts like an attribute but with some extra functionality.

class students:

  def __init__(self, phy, chem, math):
    self.phy = phy
    self.chem = chem
    self.math = math

  @property
  def percentage(self):
    return (self.phy + self.chem + self.math) / 300 * 100


stu_1 = students(90, 80, 70)
print(stu_1.percentage)
stu_1.math = 100
print(stu_1.percentage)