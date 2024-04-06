#Class method - A class method(decorator) is bound to the class & receives the class as an implicit first argument. It helps to assign fixed values in a class.

#Note: static method(decorator) can't access or modify class state & generally for utility.
#Example -
class Student:
    @classmethod #decorator
    def college(cls):
        pass

#Trying different ways to change the attribute name of class and method using changeName()
#Example -
print("Method - 1")
class Person:
    name = "anonymous" #default class name attribute

    def changeName(self, name):
        self.name = name #object name #It doesn't replace the class name attribute value

        #Person.name = name  #It replaces name value with "kamal" as we are changing class name attribute
p1 = Person()
p1.changeName("Kamal")
print(p1.name)
print(Person.name)

#Another way to change attribute name using self.__class__attribute
print("Method - 2")
class Person:
    name = "anonymous" #default class name attribute

    def changeName(self, name):
        self.__class__.name = "Rahul" #Here __class__ means Person class(object's class)

p1 = Person()
p1.changeName("abc")
print(p1.name) #Method attribute
print(Person.name) #class attribute

#Types of methods in python are - static methods, class methods(class), instance methods(self)

#Another way of above program using classmethod decorator
print("Method - 3 using classmethod decorator")
class Person:
    name = "anonymous"

    """
    def changeName(self, name):
    self.__class__.name = "Rahul" 
    """
    #or

    @classmethod #decorator
    def changeName(cls, name): #cls object refers to class
        cls.name = name

    p1 = Person()
    p1.changeName("abc")
    print(p1.name) #Method attribute
    print(Person.name) #class attribute