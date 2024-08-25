# Multi-Level Inheritance: - One parents class and two child class, and the last child can be access the parent class of parent class.

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

class Fortuner(Toyota):
  def __init__(self,type):
    self.type = type

car_1 = Fortuner("Diseal")
print(car_1.type)
car_1.stop()


#Multiple Inheritance: - In this type of inheritance, a class can inherit from more than one parent class.

class A:
    var_A = "This Is Var a"

class B:
    var_B = "This Is Var B"

class C(A,B):
    var_C = "This Is Var C"
c1 = C()
print(c1.var_C)
print(c1.var_B)
print(c1.var_A)


