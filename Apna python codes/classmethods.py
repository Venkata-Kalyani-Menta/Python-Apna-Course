#Methods are functions that belong to objects.
#So, a class has data(attributes) and methods(functions) 
class Student:
    college_name = 'ABC College'

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self): #user defined method in python
        print('Welcome student')

    def get_marks(self):
        return self.marks

s1 = Student("xyz", 54)
s1.welcome()
print(s1.get_marks())