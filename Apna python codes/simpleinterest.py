p = float(input("p : "))
r = float(input("r : "))
t = float(input("t : ")) 
si = (p * r * t) / 100
print("Interest = ",si)

#To comment multiple lines at a time, select those lines and use (Ctrl+/) shortcut.
# print("Hello")
# print("Hi")
# print("Hola")

print(4 ** 5) #Power

#type conversion(Implicit)
a, b = 2, 4.5
sum = a + b
print(sum)

#typecasting(Explicit)
a = int("2") 
b = 5.5
sum = a + b
print(sum)
print(type(a))


name = input("Enter name : ")
age = int(input("Enter age : "))
marks = float(input("Enter marks : "))
print("Welcome",name, "Age =", age, "Marks =", marks)