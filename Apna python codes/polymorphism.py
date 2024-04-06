#Polymorphism - Also called as overloading. There is operator overloading in polynorphism. When the same operator is allowed to have different meanings according to context.

#check about different dunder functions in python documentation.
#Some of the Operators and dunder functions are -
"""
a+b #addition a.__add__(b)
a-b #subtraction a.__sub__(b)
a*b #addition a.__mul____(b)
a/b #division a.__truediv____(b)
a%b #modulo division a.__mod____(b)
"""
print(1 + 2) #3
print("apna"+"college") #concatenate 
print([1,2,3] + [4,5,6]) #lists merge

#Creating a function with complex numbers operations and also using operator overloading. Here, real and img are predefined variables in python.
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2): #Built in Dunder addition method
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2): #Built in Dunder subtraction method
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
num1 = Complex(1, 3)
num1.showNumber() #To display first complex number

num2 = Complex(4, 6)
num1.showNumber() #To display second complex number

num3 = num1 + num2
num3.showNumber() #Sum of two complex numbers