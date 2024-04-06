#Loops are used to repeat instructions.
i = 1
while i <= 5: #Stopping condition
    print("hello")
    i += 1
print(i)
print("Loop ended")

#Print a table
n = int(input("Enter a number : "))
i = 1
while i <= 10:
    print(n, "*", i, "=", n * i)
    i += 1

#Print the elements of a list using a loop(traverse)
print("List elements")
i = 0
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
while i <= len(list)-1:
    print(list[i])
    i += 1

#Print strings from a list
print("List elements")
i = 0
list = ["apple", "banana", "kiwi"]
while i <= len(list)-1:
    print(list[i])
    i += 1
print("end of loop")

#Searching an element in a list/tuple
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
s = 36
i = 0 #initialization
while i < len(tup):
    if(tup[i] == s):
        print(s, "found at index", i)
        break
    else:
        print("not found")
    i += 1
print("end of loop")

#Using break 
i = 1
while(i <= 5):
    print(i)
    if(i == 3): 
        break #break helps to exit from every loop/condition
    i += 1
print("end of loop")

#Using continue - To print odd numbers from 1 to 10
i = 1
while(i <= 10):
    if(i % 2 == 0):
        i += 1
        continue #skip this turn
    print(i)
    i += 1
print("end of loop")

#Using continue - To print even numbers from 1 to 10
i = 1
while(i <= 10):
    if(i % 2 != 0):
        i += 1
        continue #skip this turn
    print(i)
    i += 1
print("end of loop")


