#set methods - set is mutable, but its elements are immutable
set1 = set() #empty set

#adds an element
set1.add(1)
set1.add(2)
set1.add("hello")
set1.add(2)
print(set1)

#removes the element 
set1.remove(2) #if you try to remove an unexisting element in a set then it shows key error.
print(set1)

#empties the set
set2 = {1, 2, 4.1, True}
print(set2)
set2.clear()
print(len(set2))
print(set2) #empty set

#removes a random value Apna
set2 = {1, 2, 4.1, True}
print(set2.pop()) #Returns the popped element from a set.
print(set2)
print(set2.pop())
print(set2)

#combines both set values & returns new
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1)
print(set2)

#combines common values & returns new
print(set1.intersection(set2))

