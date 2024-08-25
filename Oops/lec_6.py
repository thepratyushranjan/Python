# Super() Method:- Its used to access methods of the parent class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display(self):
        print(f"{self.make} and {self.model} and {self.year}")

class Truck(Car):
    def __init__(self, make, model, year, engine, window):
        super().__init__(make, model, year)
        self.engine = engine
        self.window = window

car = Truck("Ford", "BMW", "2021", 2000, 2000)
print(car.make)
print(car.model)
print(car.year)
car.display()
print(car.engine)
print(car.window)
