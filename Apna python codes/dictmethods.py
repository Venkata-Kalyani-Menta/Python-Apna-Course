#Methods in dict
stud = {
    "name" : "kamal",
    "sub" : {'Accounts' : 100, 'Costing' : 78}, #Creating a key as sub dictionary. 
    "Rno" : 1 
}
print(stud.keys()) #myDict.keys() - returns all keys
print(list(stud.keys())) #We are typecasting here, dictionary keys into list datatype. We can also typecast to tuple datatype also. Example - typecast int to float --> float(9).
print(tuple(stud.keys()))
print(len(stud)) #Printing the total number of key-value pairs in a dictionary using len()
print(len(list(stud.keys())))

print(stud.items()) #myDict.items() - returns all (key, val) pairs as tuples

print(list(stud.items())) #converting and Printing dict items as list items
pairs = list(stud.items()) #creating a new list and accessing list items
print(pairs)
print(pairs[0])

#myDict.get(“key“) - returns the key according to "value"
print(stud["name"]) #If unexisted key is given in this way, it shows error and otherwise shows as dict value.
#print(stud["name2"]) --> error
print(stud.get("name")) #If unexisted key is given in this way, it shows output as None and otherwise it shows dict value. So, using methods in python is preferred to avoid unwanted errors and execute remaining code with no errors.
print(stud.get("name2")) #no error --> None 

print(stud.values()) #myDict.values() - returns all values

print(stud.update({"city" : "nellore"})) #myDict.update(newDict) - inserts the specified items to the dictionary. Used to append new key value pair or replace new value in a key within a dictionary
print(stud)
stud.update({"name" : "kalyani"}) 
print(stud)
#You can also update key value pairs in a dictionary using a new dictionary
new_dict = {"name" : "hari", "age" : 23} #If same key is existed in the previous dictionary, then it overwrites the key with new value given.
stud.update(new_dict) #Updating a dictionary using another dictionary.
print(stud)
