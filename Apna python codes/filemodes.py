f = open("demo1.txt", "r+") #This mode overwrites the existing file contents in the beginning of the text file. Previously, it has contents "I am learning python"
f.write("abc") #After this line, it has contents "abcm learning python". Because r+ modes starts from the beginning of the file. Obviously, r+ overwrites/replaces contents upto the length of new text. But w/w+ mode clears/truncates everything in the existing file and again starts from the beginning of the file.
print(f.read()) #Because the file pointer ends at the end of "abc" in the text after writing. So, it reads remaining text from there onwards. "m learning python" is the result.

f = open("demo1.txt", "a+")
f.write("xyz") #After appending the text, there the pointer is at the EOF position so there is nothing to read here.
print(f.read())
f.close()