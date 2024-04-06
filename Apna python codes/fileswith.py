#We can use 'with' and 'as' keywords in files to create alias names for file operations.
#Previously "demo2.txt" has "hello files"
#with syntax as shown below examples - 
with open("demo2.txt", "r") as f:
    data = f.read()
    print(data) # "hello files"

with open("demo2.txt", "w") as f:
    f.write("Hello data!") #Overwrites file as "Hello data!"
f.close()