#Inheritance - When one class(child/derived) derives the properties & methods of another class(parent/base).
#Single inheritance example
print("Single inheritance")
class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car): #Inheriting base class Car into new class ToyotaCar
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

car1.start() 
car2.stop()
print(car2.color)
print(car1.name)

#3 types of inheritance - Single, Multiple, Multi-level inheritance
#Multi-level inheritance
print("Multi-level inheritance")
class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
car1.start()

#Multiple inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

#Super method - super() is used to access methods of the parent class
print("Super class")
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started.")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("Prius", "Electric")
print(car1.type)