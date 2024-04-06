a = int(input("Enter a number = "))
b = int(input("Enter a number = "))
c = int(input("Enter a number = "))

if(a >= b and a >= c):
    print("First number is greatest.")
elif(b >= c):
    print("Second number is greatest.")
else:
    print("Third number is greatest.")