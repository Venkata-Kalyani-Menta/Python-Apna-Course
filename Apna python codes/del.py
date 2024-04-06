#Delete an object using del keyword
#syntax - del obj (or) del obj.attr 
class Student:
    def __init__(self, name):
        self.name = name
        
s1 = Student("abc")
print(s1) #Printing existing object
print(s1.name)

del s1.name #Deleting name attribute
#print(s1.name) #Shows error as name is not existed.

del s1 #Deleting s1 object
#print(s1) #Shows error as s1 object is not existing.