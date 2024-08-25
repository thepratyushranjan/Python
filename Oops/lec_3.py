#Encapuslation: Encapsulation is the process of bundling data and methods that work on that data within a single unit.
# Public: Accessible from anywhere (default in Python).
# Protected: Indicated with a single underscore _attribute. It's a convention that suggests the attribute shouldn't be accessed directly, but it can be accessed if needed.
# Private: Indicated with double underscores __attribute, making it more hidden and harder to access directly from outside the class.
class Car:
    def __init__(self, model, speed, engine):
        self.model = model  # Public attribute
        self.__speed = speed # Protected attribute
        self._engine = engine  # Private attribute

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed > 0:
            self.__speed = speed
        else:
            print("Must be positive")

    def get_engine(self):
        return self._engine

car =  Car("Toyota", 100, "V6")
print(car.get_speed())
print(car.get_engine())
print(car.set_speed(0))
car.set_speed(-50)