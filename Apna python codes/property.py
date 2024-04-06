#Property decorator - We use @property decorator on any method in the class to use the method as a property. It helps to change the class attributes to latest values when any change is required.

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property #decorator
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stud1 = Student(98, 97, 99)
print(stud1.percentage)

stud1.phy = 86 #Without using property decorator, it doesn't change previous object percentage value. And it shows old results. So, this decorator helps here.
print(stud1.percentage)

#If you want to explore some other decorators, you can check @getter and @setter 