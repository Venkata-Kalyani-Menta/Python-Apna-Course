#Python can be used to perform operations on a file. (read & write data)
f = open("demo.txt", "r+") # text in "demo.txt" file is "Hello python"

"""
#Check this code once to read entire file contents
data = f.read()
print(data)
"""

data = f.read(6) #It reads upto 6 characters from the file. "Hello "
print(data)

data1 = f.readline() #It reads the text line of the pointer from where it stopped. After reading the end of the textline, if there is nothing to read then it prints newline (\n). Beacause every end of the line text in a file has a newline character.
print(data1)

#f.write("\nI am learning python") #Use it once to write the new text in the existing file.

data1 = f.readline() 
print(data1)

data1 = f.readline() #There is nothing to read next line so, it prints newline character.
print(data1)

f.close()