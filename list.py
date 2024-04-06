"""
Lists is a built-in datatype that stores set of values.
It can store elements of different types. They are mutable.
"""
student = ["karan", 23, 10]
print(student)
print(len(student)) #gives list length
print(type(student))

student[0] = "arjun"
print(student)
print(student[2]) #if you give index not between (0 to length - 1) then "list index out of range" error is displayed.

#List slicing. In output ending index value is not displayed.
marks = [87, 64, 33, 95, 76]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

#List Methods. To study more about lists and methods, check python documentation.
list = [2, 1, 3]
list.append(4) #adds one element at the end.
print(list.append(5)) #It displays list result as None and not the list but append operation is performed. 
print(list)

list.sort() #sorts in ascending order.
print(list)
print(list.sort())

list.sort(reverse = True) #sorts in descending order.
print(list)

list.reverse() #reverses list. 
print(list)

list.insert(3, 5) #insert element at index. insert(index, element)
print(list)

list1 = ['c', 'e', 'a', 'g', 'f', 'b']
list1.sort()
print(list1)
list1.reverse()
print(list1)

print(list)
list.remove(5) #removes first occurence of element
print(list)
list.pop(3) #removes element at index.
print(list)