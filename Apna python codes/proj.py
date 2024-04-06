#Creating a small project in python 
#Guess the number - User inputs any number and it should match system generated random number(target). If not matching, then show either bigger or smaller numbers to guess.

#Here we use random module which contains randint() function to generate random numbers of integer type.
import random
target = random.randint(1, 100) #Generates any random number from 1 to 100.

while True:
    userChoice = input("Guess the target or Quit : ")
    if userChoice == "Quit":
        break

    userChoice = int(userChoice)
    if userChoice == target:
        print("Success : Correct Guess!!")
        break
    elif userChoice < target:
        print("Your number was too small. Take a bigger guess..")
    else:
        print("Your number was too big. Take a smaller guess..")

print("----GAME OVER----")