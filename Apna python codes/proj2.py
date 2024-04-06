#Creating a Random Password Generator Project 
import random
import string #Collection of string constants.

#val = random.choice(["abc", "def", "xyz"]) #You can give any datatype of values in a list. 
#print(val) #This will print any random characters in above list given like "abc" or "def" or "xyz".

#print(string.ascii_letters) #Output - abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW So, we used predefined string variables here to print alphabets. Like this there are for digitS, punctuations, ascii_uppercase and ascii_lowercase etc.

#So, in a password to mix different characters we combined all available string constants.
pass_len = 8 #Password Length required. 
charValues = string.ascii_letters + string.digits + string.punctuation

#Using list comprehension. syntax - [function for i in range(n)] to reduce the number of lines in python code.

#random.choice() is used to generate random password here
password = "".join([random.choice(charValues) for i in range(pass_len)]) 

#password = "*".join([random.choice(charValues) for i in range(pass_len)]) - output shows characters with some '*' characters also and password length also changes. We can give symbols to join strings. We used string join() to combine mixed characters to an empty string to generate password output. Otherwise, it gives output in list format.

#Detailed code explanation for above list comprehension used.
#password = ""
#for i in range(pass_len):
#    password += random.choice(charValues)

print("Your random password is:", password)