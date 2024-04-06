print("Hello world")
print(45)
print("hello", "hi", 56+89)
name = "Khalyanni"
age = 56
print(name)
print(type(name))
print(type(age))
n1 = 'abc'
n2 = "bcd"
n3 = '''hi'''
print(n1, n2, n3)
a = True
print(type(a))   
b = None
print(type(b))
age = 43
print(type(age))  
x = 56
y = 45
sum = x+y
print(sum)
A, B = 2, 3
txt = "@"
print(2 * txt * 4)
A, B = "2", 3
txt = '@'
print((A+txt) * 3)
A, B = 2, 3
C = 5
print(A+B*C)
A, B = 10.6, 7
c = A*B
print(c)
A, B = 5, 6
C = A//B  #this floor division operator rounds off to nearest integer(lesser/equal value)
print(C, A/B)
A, B = 12, 6
c = A//B
print(c)
A, B = -12, 6
c = A//B
print(c)
A, B = 12, -6
c = A//B
print(c)
X, Y = 17, 6
c = X % Y
print(c)
X, Y = -16, 6
c = X % Y
print(c)
X, Y = 17, -6 #If denominator is -ve then in remainder(modulo) division, result is -ve 
c = X % Y
print(c)
#print("Hello")
A, B = 1.5, 3
C = A//B
print(C, A/B)
A, B = -12, 5
C = A//B #Floor division considers the smallest integer value if result gives in decimal.
print(C, A/B) #-2.4 is nearest to -3.
print(2 ** 5) #Power operator