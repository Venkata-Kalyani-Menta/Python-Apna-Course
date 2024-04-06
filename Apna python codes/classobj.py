"""OOPS in python -
To map with real world scenarios, we started using objects in code.
This is called object oriented programming"""

#Class - Class is a blueprint for creating objects.
#creating class
class Student: #creating student class
    name = "abc def"

#creating object (instance of class)
s1 = Student() #s1 is an object of student class
print(s1.name)
print(s1) #Prints the name of the main

s2 = Student() #s2 is an object of student class
s2.name = "xyz"
print(s2.name)

#__init()__ - It is a default constructor in a class - All classes have a function called __init__(), which is always executed when the object is being initiated.
#Constructor - The constructor is invoked/executed at the time of object creation. The self parameter is a default reference to the current instance(object) of the class, and is used to access variables that belongs to the class.
class Car:
    name = "Mercedes"
    def __init__(self): #default constructor. And in the place of self we can name it with different names also. Like, "def __init__(abcd):"
        print(self)
        print("Adding new car object in database...")

c1 = Car()
print(c1)
print(c1.name)

#Using parameterized constructor
class Fruit:
    def __init__(self, name):
        self.name = name
        print("Adding new fruit object in database...")

f1 = Fruit("Apple")
print(f1.name)

f2 = Fruit("Mango")
print(f2.name)

#The data like variables and other data that stores within an object are called as attributes. There are 2 types of attributes like class and object attributes.

class Student:
    college_name = "ABC College" #Class attribute
    name = "Anonymous"
    def __init__(self): #default constructor
        pass

    def __init__(self, name, marks): #parameterized constructor
        self.name = name #Here, if same name is present in both class and object attributes then (obj attr > class attr) is given preference to execute. Because current object attribute gets more preference.
        self.marks = marks
        print("Adding new student in database...")

s1 = Student("Karan", 97)
print(s1.name, s1.marks)

s2 = Student("Kamal", 98)
print(s2.name, s2.marks)
print(s2.college_name)

s3 = Student("abc", 78)
print(s3.name)