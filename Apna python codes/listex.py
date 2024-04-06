#Ask user to enter 3 movies and put it in a list.
movies = []
movies.append(input("Enter movie1 name = "))
movies.append(input("Enter movie2 name = "))
movies.append(input("Enter movie3 name = "))
print("List of movies =", movies)

#Write a program to check if a list contains a palindrome of elements or not. Also use copy() method.
list = [1, 2, 3]
print(list)
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrome")
else:
    print("Not palindrome") 

list1 = ['r', 'a', 'c', 'e', 'c', 'a', 'r']
print(list1)
copy_list = list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("palindrome")
else:
    print("Not palindrome") 
