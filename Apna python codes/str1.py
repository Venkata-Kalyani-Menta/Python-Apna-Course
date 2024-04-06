#Types of strings
str1 = 'This is a string' #We can access values in strings, but cannot be modified.(Immutable strings)
str2 = "This is a string"
str3 = """This is a string""" #Previlege to use within strings with single and double quotes.To avoid confusion.

str1 = "This is a string.\nWe are creating it in python."
print(str1)
str2 = "Programming"
print(str1 + " "+ str2)
print(len(str2))
print(str1[4])

#Slicing - Accessing parts of a string
str = "Python"
print(str[1 : 4])
print(str[ : 4]) #or str[0 : 4] 
print(str[1 : ]) #or str[1 : len(str)]
#Negative indexing
print(str[-5 : -1])