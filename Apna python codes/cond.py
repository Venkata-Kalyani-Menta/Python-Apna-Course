#if-elif-else conditional statement.
light = input("Enter light color = ")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("Light is broken.")
    
    
#Ternary operator / Single line if 
#Syntax - <var> = <val1> if <condition> else <val2>
food = input("food : ")
eat = "Yes" if food == "cake" or food == "apple" else "no" 
print(eat)
"""
#Statement form - syntax - <st1> if <condition> else <st2>
#print("yes") if food == "cake" or food == "apple" else print("no") 
"""

#Clever if / Clever Ternary Operator Ex-1
#Syntax - <var> = (false_val, true_val) [<condition>]
age = int(input("age : "))
vote = ("no", "yes") [age >= 18] #The statement in [] is condition. () has True and False outputs.
print(vote)

#Clever if / Clever Ternary Operator Ex-2
sal = float(input("salary : "))
tax = sal * (0.1, 0.2) [sal > 50000] #if sal < 50000, 10% tax else 20% tax.
print(tax)