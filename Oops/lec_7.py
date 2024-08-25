# Method Overloading: - Method Overloading is a concept where multiple methods have the same name but different parameter (different number or type of arguments).
# However, Python does not support method overloading in the traditional sense as seen in some other programming languages like Java.

class Example:
    def greet(self, name=None):
        if name is not None:
            return f"Hello, {name}"
        else:
            return "Hello, World!"
obj = Example()
print(obj.greet())
print(obj.greet("Thanos"))

# Explanation:
# The greet method can be called with or without a parameter.
# When no argument is provided, it returns a generic greeting.
# When a name is provided, it returns a personalized greeting.

# Method Overriding occurs when a subclass provides a specific implementation of a method that is already defined in its parent class.
# The subclass's method will replace the parent class's method with the same name.

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Bark
print(cat.speak())  # Output: Meow

#Explanation:

# Animal class has a method speak().
# Both Dog and Cat classes inherit from Animal and override the speak() method.
# Dog class’s speak() method returns "Bark", and Cat class’s speak() method returns "Meow".
# The specific implementation in the subclass is used when the method is called on an instance of that subclass.
