#range in python - range() is a built-in function in python. It also considered as a datatype in python. It is commonly used in for loops.
#syntax - range(start?, stop, end?). In this syntax, ? means optional to use.
print("Range in python\nOutput 1")
for i in range(10): #range(stop) It doesn't include stop value. By default, without start value, it starts from 0.
    print(i)

print("Output 2")
for i in range(2, 10): #range(start, stop)
    print(i)

print("Output 3")
for i in range(2, 10, 2): #range(start, stop, step) step helps for increment/decrement values in a loop.
    print(i)

print("Output 4")
for i in range(10, 0, -1):
    print(i)

#Print even and odd numbers from 1 to 100 using the range()
print("Even numbers from 1 to 100")
for i in range(0, 101, 2):
    print(i)
print("Odd numbers from 1 to 100")
for i in range(1, 100, 2):
    print(i)

#search for a number using range()
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
key = 36 #check output if key = 33
for i in range(len(tup)):
    if(tup[i] == key):
        print(key,"is found at index", i)
        break
else:
    print("End of search")


seq = range(10) #Instead of writing these two lines, you can type as "for i in range(10)"
for i in seq:
    print(i)

for i in range(1, 101): #Printing values from 1 to 100
    print(i)

for i in range(100, 0, -1): #Printing values from 100 to 1
    print(i)

#printing a multiplication table using range
n = int(input("Enter a number = "))
for i in range(1, 11):
    print(n * i)

#pass is a null statement that does nothing. It is used as a placeholder for future code.
for i in range(10):
    pass #It does nothing work. Otherwise, if we don't use pass statement, it shows intended block error.

#To print sum of natural numbers using range and for
n = int(input("Enter a number = "))
sum = 0
for i in range(1, n+1):
    sum += i
print("sum of natural numbers =",sum)

#To print sum of natural numbers using while
n = int(input("Enter a number = "))
sum = 0
i = 1
while (i <= n):
    sum += i
    i += 1
print("sum of natural numbers =", sum)

#Find Factorial of a number using while loop 
n = int(input("Enter a number = "))
fact = 1
i = 1
while (i <= n):
    fact *= i
    i += 1
print("factorial of", n, "=", fact)

#Factorial of a number using for loop and range()
n = int(input("Enter a number = "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("factorial of", n, "=", fact)
