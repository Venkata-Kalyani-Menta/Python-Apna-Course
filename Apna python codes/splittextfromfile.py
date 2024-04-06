with open("nums.txt", "r") as f:
    data = f.read()
    print(data)

#splitting data into individual numbers and add them to the empty string without using split()
num = ""
for i in range(len(data)):
    if (data[i] == ","):
        print(int(num)) #if you don't typecast then all strings will print with spaces if there are spaces between text in the file. Now, here we have converted individual strings to integers using the loop.
        num = ""
    else:
        num += data[i]
print((num)) #to print the last number from data
print(data)
print(type(data))
f.close()