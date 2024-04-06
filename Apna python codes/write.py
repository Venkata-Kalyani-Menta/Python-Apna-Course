f = open("sample.txt", "w+") #If 'w' or 'a' mode is given for unexisting file, then on executing the program, it will create that new file. + is used for both reading and writing the file.

f.write("Hello, World!")
f.seek(0) #If you don't put seek to the beginning of the file, then it won't show output the file because by default after writing the file, it will automatically points the cursor to the end of the file, so there is nothing to print the text. So, again we should change the file pointer to the start using seek(). syntax - seek(n). Here, n means nth character of text.
data = f.read()
print(data)

f = open("sample.txt", "a+")
f.write("\nI am learning about files in python.")
data = f.read()
print(data)

f.write("\nI know tuples, dict.")
f.seek(0)
data = f.readline()
print(data)
f.close()
