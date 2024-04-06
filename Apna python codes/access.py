#Private attributes and methods are meant to be used only within the class and are not accessible from outside the class. So, that variable/method is mentioned with two underscores(__) within the class/function.
#let us try to access bank account information using private attributes.
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #private acc_pass
    def reset_pass(self):
        print(self.__acc_pass) #Accessible within the class

acc1 = Account("12345", "abcde")
acc1.reset_pass()
#print(acc1.__acc_pass) #Not accessible outside of class

#Example 
class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())
#p1.__name #Private Attribute error
#p1.__hello() #Private Attribute error
