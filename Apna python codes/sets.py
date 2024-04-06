#Set is the collection of the unordered items.
#Each element in the set must be unique & immutable.

null_set = set() #empty set syntax. If you assign as {} instead of set() in an empty variable, then it becomes a dict datatype.
print(type(null_set))
print((null_set))

null_set = {}
print(null_set)
print(type(null_set))

nums = {1, 2, 3, 4}
print(type(nums))
print(nums)

#repeated elements stored only once, so it resolved to {1, 2}
set2 = {1, 2, 2, 2}
print(set2)

set2 = {1,2,3,2,2,"world","world","hello"} #Shows unique and unordered elements in a set.
print(set2)
print(len(set2)) #Total unique set items

#The different datatypes like float, int, boolean, strings, tuple can be stored in a set. Because they are immutable. But mutable types like list and dict cannot be stored in a set because they should be unique, otherwise unhashable(mutable) error occurs.
set1 = {1,2,3,"str"}
print(set1)

set3 = {9, 9.0} #considers 9 and 9.0 as same value instead of int and float value.
print(set3)

set3 = {9, '9.0'} #Now we convert one value into string and doesn't consider as same values
print(set3)

set3 = {('int', 9), ('float', 9.0)}
print(set3)