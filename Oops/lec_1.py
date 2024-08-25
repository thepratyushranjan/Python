# Class:- A Class is blueprint or a template for creating objects.
# Object:- Objects is a real world entity.
# Example:-
class Car:
    color = 'blue'
    model = 'BMW'


car = Car()
print(car.color)
print(car.model)

# __init__ :- It is a Constructor.its always executed when object initiated
# this is way define constructor. and bracketed value is called parameter.

class Student:
    college = 'REC Azamgarh' # Class Attribute which is common attribute

    # 1:- Default Constructor
    def __init__(self):
        print("Default Constructor")

    # 2:- Parameterized Constructor
    def __init__(self, age, name, marks):
        self.age = age  # This is called is object attribute and object attribute > Class Attribute
        self.name = name
        self.marks = marks
# Methods:- In class write the function it's called the method
    def display(self):
        print(f" Student is {self.name} and age is {self.age} and marks is {self.marks}")


# Static Method:- it's not used self parameter (its Working a like class.)
# This is a decorator:- its taking input a function and return a function.

    @staticmethod
    def hello():
        print("Hello Students")

data_of_student = Student(10, "Tony Stark", 10)
print(data_of_student.age)
print(data_of_student.marks)
print(data_of_student.marks)
data_of_student.display()
data_of_student.hello()