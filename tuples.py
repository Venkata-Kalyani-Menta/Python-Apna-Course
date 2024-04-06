#Tuples is a built-in datatype that lets us create immutable sequences of values.
tup = (2, 1, 3, 1)
print(type(tup))

tup1 = () #Empty tuple
print(tup1)
print(type(tup1))

tup2 = (1,) #To consider a single element tuple, put comma. otherwise it will take as an integer.
print(tup2)
print(type(tup))

tup3 = (1) #tup3 is not a tuple here. It's just an integer.
print(tup3)
print(type(tup3))

tup3 = ("hello") #tup3 is not a tuple here. It's just a string.
print(tup3)
print(type(tup3))

tup3 = (1.0) 
print(tup3)
print(type(tup3))

tup3 = ("hello, ") #tup3 is a tuple
print(tup3)
print(type(tup3))

#Tuple methods
tup = (2, 1, 4, 1)
print(tup[1:3])

print(tup.index(2)) #returns index of first occurence.
print(tup.count(1)) #counts total occurrences
