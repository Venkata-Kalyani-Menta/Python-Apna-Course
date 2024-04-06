print("hello")
#Peculiar behaviour of modulo remainder(%) operator in python.
a, b = -12, 6
c = a%b 
print(c)

a, b = 17, 6
c = a%b 
print(c)

a, b = 3, 6
c = a%b 
print(c)

a, b = -14, 6 # Modulo subtracts the numbers and gives result if (n1 > n2) and n1 is -ve. Instead of normal output. (12 < 14 < 18), so 18 - 15 = 3 as per in next multiples of 6.
c = a%b
print(c)

a, b = -4, 6 # Modulo subtracts the numbers and gives result if (n1 < n2) and n1 is -ve. Instead of normal output. so, 6 - 4 = 2
c = a%b 
print(c)

a, b = 12, -6
c = a%b 
print(c)

a, b = 15, -6 #If n2(denominator) is -ve, result is also -ve. (n1 > n2) Subtracts from next available multiple of 6. (12 < 15 < 18), so 18 - 15 = 4.
c = a%b 
print(c)

a, b = 2, -6 #If n2(denominator) is -ve, result is also -ve. (n1 < n2) 6 - 2 = 4
c = a%b 
print(c)