# Abstractions: Abstraction is the concept of hiding complex implementation details and showing only the necessary parts of an object or function.
class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def drive(self):
        print(f"This car {self.name} drives self which color is{self.color} and mmodel is {self.model}")

car_1 = Car("BMW", "X5", "Black")
car_1.drive()
print(car_1.name)
print(car_1.model)
print(car_1.color)

