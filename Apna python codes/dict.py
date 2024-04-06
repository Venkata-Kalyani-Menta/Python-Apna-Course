"""
Dictionaries are used to store data values in key:value pairs
They are unordered, mutable(changeable) & don't allow duplicate keys
"""
#dict datatype
data = {
            "name" : "abc", #Any key and value pairs are mutable and interchangeable in dictionary datatypes in python.
            "age" : 23,
            "price" : 32.3,
            "subjects" : ["C", "Java", "Python"], 
            "marks" : (56, 65, 75), #Tuples cannot be interchangeable as key and value pairs.
            1 : "cde", #We can give any kind of keys with different datatypes in dictionary but, it should me meaningful to understand. 
            34.4 : 3
       }
print(data)
print(type(data))

print(data["age"]) #We can access values in a dictionary using keys only. Not using index values. 
print(data["subjects"])
print(data["marks"])

#We can modify values of keys by assigning new values. Overwrite existing values with new values.
data[1] = "fgh"
print(data)

#Create an empty dictionary and create new key and value pairs.
new_dict = {}
print(type(new_dict))
new_dict["name"] = "aparna"
new_dict['age'] = 24
print(new_dict)

#How to enter marks of a student in a dictionary?
dict1 = {}

x = int(input("Enter phy marks : "))
dict1.update({"phy" : x})
x = int(input("Enter math marks : "))
dict1.update({"math" : x})
x = int(input("Enter phy marks : "))
dict1.update({"chem" : x})
print(dict1)

#Example to store dictionary meanings in a dictionary variable using key value pairs.
dict4 = {
     "table" : ["a piece of furniture", "list of facts & figures"],
     "cat" : "a small animal"
        }
print(dict4)
