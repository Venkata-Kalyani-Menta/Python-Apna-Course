marks = int(input("Enter student marks = "))

if(marks >= 90): #indentation
    grade = 'A'
elif(marks >= 80 and marks < 90):
    grade = 'B'
elif(marks >= 70 and marks < 80):
    grade = 'C'
elif(marks >= 50 and marks < 70):
    grade = 'D'
else:
    grade = 'E'
print("grade =",grade)
