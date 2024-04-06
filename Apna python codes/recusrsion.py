#Recursion - When a function calls itself repeatedly, it is recursion.
#Recursion Example
def show(num):
    if (num == 0): #Base condition to stop recursion otherwise it becomes like error as infinite recursion
        return
    print(num)
    show(num - 1)
    print("END") #To indicate the end of each call stack from 4 to 1 in this example

show(4) #Function call

#Factorial program using recursion
def fact(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return num * fact(num - 1)
    
print(fact(5))

#Print list elements using recursion
def print_list(list, idx = 0): #idx means index value parameter by default given as 0
    if (idx == len(list)): 
        return 
    print(list[idx])
    print_list(list, idx + 1)

fruits = ["mango", "apple", "banana"]
print_list(fruits)

#Print sum of n natural numbers using recursion
def print_sum(n):
    if(n == 0):
        return 0
    return print_sum(n - 1) + n

sum = print_sum(10)
print(sum)
