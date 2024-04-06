#Creating a nested dictionary
stud = {
    "name" : "kamal",
    "sub" : {'Accounts' : 100, 'Costing' : 78}, #Creating a key as sub dictionary. 
    "Rno" : 1 
}
print(stud)
print(type(stud))
print(stud['sub'])
print(stud["sub"]["Costing"]) #Accessing values from sub/nested dictionary.
print(stud["Rno"])