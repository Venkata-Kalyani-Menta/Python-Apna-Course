#Loops are used used for sequential traversal. For traversing list, string, tuples etc.
#for loop
#Traverse process
t = ("apple", "banana", 3, 3.4)
for i in t:
    print(i)

str = "hello"
for ch in str:
    print(ch) 

#for loops using else - helps to end the loop
str = "hello world"
for ch in str:
    if ch == 'o': #check the output with non-existing element. Like ch == 'u' etc
        print("o found")
        break #else statement doesn't work with break. If search element is found.
    print(ch)
else: #work when loop ends.
    print("end")


#Finding element within a tuple
t = (1, 4, 9, 16, 25, 64, 36, 49, 64, 81, 100)
s = 64
i = 0 #index
for ele in t:
    if(ele == s):
        print("element found at index", i)
        #break  #if you put break here, then it prints element is found for the first time only.
    i += 1
print("end")
