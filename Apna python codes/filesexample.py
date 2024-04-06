#Create a file "pracice.txt" with some data
with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")

"""Output is -
Hi everyone
we are learning File I/O
using Java.
I like programming in Java."""

#So, we are replacing the occurences of above previous text "Java" with "Python" using string function replace() and overwriting the text in the same file "practice.txt"

with open("practice.txt", "r") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")
with open("practice.txt", "w") as f:
    f.write(new_data)

"""New output -
Hi everyone
we are learning File I/O
using Python.
I like programming in Python."""

#Search if the word “learning” exists in the file or not. we are using a function
def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if (data.find(word) != -1): #or simply use - if(word in data)
            print("Found word")
        else:
            print("Word not found")
check_for_word()

#Write a function to find in which line of the file does the word “programming” occur first.
#Print -1 if word not found.
def check_for_line():
    word = "programming"
    data = True #To start the loop, we need to assign True. If we give empty string then loop doesn't work.
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data): 
                print(line_no)
                return
            line_no += 1
    return -1 #If line not found. To know if line is not found then call as print(check_for_line())
check_for_line()

f.close()