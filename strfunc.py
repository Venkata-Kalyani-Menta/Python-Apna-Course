#String functions
#endswith("str") - returns true if string ends with substring
str = "I am a coder."
print(str.endswith("ring"))

#capitalize() - capitalizes 1st char in given string
str = "hello"
print(str.capitalize())
print(str)
str = str.capitalize()
print(str)

# replace(old, new) - replaces all occurrences of old with new
str = "Hello python"
print(str.replace("l", "p"))
print(str.replace("python", "java"))

# find(word) - returns 1st index of first occurrence of string
print(str.find("o"))
print(str.find("pyt"))
print(str.find("a")) #Returns -1 when that string doesn't exist. Invalid index.

# count("substr") - counts the occurrence of substr in string
print(str.count("o"))
print(str.count("py"))
print(str.count("apple")) #Returns 0 if doesn't exist.

str = "Hi, I am $abc price 45$ 67$"
print(str.count("$"))

name = input("Enter your name : ")
print("Length of str =",len(name))

