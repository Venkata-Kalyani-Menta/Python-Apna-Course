#function in python is a block of statements that perform a specific task.
#syntax -
"""
def func_name( param1, param2..) :
#some work
return val
#func_name( arg1, arg2 ..) #function call
"""

#Program to write a function for addition of two numbers
def sum(a,b): #User-defined function
    s = a+b
    print(s)
    return s

sum(10, 20)

sum(20, 30)

#Another way to write a function for addition of two numbers
#Function defintion
def sum(a,b): #parameters
    return a+b 
res = sum(50, 40) #Function call; arguments
print(res)

#Another example
def print_hello():
    print("Hello")

print_hello()
out = print_hello()
print(out) #it prints None because print_hello() returns None datatype, as there is no datatype to return.

#Average of 3 numbers
def avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

avg(10, 20, 30)

#Assigning a default value to parameter, which is used when no argument is passed. In general functions, if parameters is not passed to this prod() it shows error. So, default parameters are saving from errors in a code.
#Here is an example to show product of two numbers using a default parameter
#Ex - 1
def prod(b, a = 2): #Default parameters are always assigned at the end of the remaining parameters
    p = a * b
    print(p)

prod(10, 20)
prod(6) #b = 6, a = 2 because only one parameter is passed. Another parameter is already default parameter

#Ex - 2
def mul(a = 2, b = 3):
    p = a * b
    print(p)

mul()
mul(10)

#some of the built-in(pre-defined) functions in python - If you want to study the syntax of built-in functions type them here without using comment and hover over them to view information about them.
#print() - To print something. Default seperator is space and end of line is newline.
print("Hello World", "Namaskaram", sep = ", ", end = " ") #Here, in this example different words are seperated by comma and end of the line is seperated by space.
print("ABC")

#range()
#type()
#len()

#print length of given lists
fruits = ["apple", "banana", "orange", "watermelon"]
cities = ["bengaluru", "nellore", "chennai", "vishakapatnam", "tirupati"]

def len_list(lists):
    print(len(lists))

len_list(fruits)
len_list(cities)

def print_list_sameline(list):
    for item in list:
        print(item, end = " ")

print_list_sameline(fruits)
print() #to avoid printing in same line because of print_list_sameline()
print_list_sameline(cities)
print()

#convert USD to INR
def convert(usd):
    inr = usd * 83
    print(usd, "USD =", inr, "INR")

convert(1)

#Function to return if the given value is even or odd
def is_even(num):
    if(num % 2 == 0):
        return "EVEN"
    else:
        return "ODD"
    
print(is_even(1))

