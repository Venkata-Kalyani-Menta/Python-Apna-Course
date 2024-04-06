#Define an Employee class with attributes role, department and salary. This class also should have showDetails() method

#Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role: ", self.role)
        print("Department: ", self.dept)
        print("Salary: ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", 100000)
        print("Name: ", self.name, " \nAge: ", self.age, "\n")

emp = Employee("CA", "Finance", 70000)
emp.showDetails()

engg1 = Engineer("ABC", 40)
engg1.showDetails()
