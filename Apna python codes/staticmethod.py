#Static Methods in a class - Methods that don’t use the self parameter (which work at class level)
#Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. Each decorator should start with '@'
class Student:
    @staticmethod #decorator  
    def college(): #If to use a normal function within a class without using a default/parameterized constructor, then we need to change it as static method using static method decorator.
        print("ABC College")

    def clg(self): #Default constructor
        print("xyz college")

s1 = Student()
s1.college() 
s1.clg()