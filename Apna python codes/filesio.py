f = open("demo.txt", "r") #f = open("demo.txt", "r+")
#f.write("Hello python") #creating a new file with text
data = f.read() #You could also use to read no of characters required. syntax - read([n]) n is the number of characters to read which is optional. For the first time, read() helps to read entire file and ends the pointer to the lastline, so there won't be any characters to read except the \n character. And if we try to read again the pointer stops at the end of the file and prints newline character only. 
print(data)
print(type(data))

data1 = f.read(5) #It doesn't print text. Only newline character is printed.
print(data1)

f.close()