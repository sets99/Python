import random
import time

# define a dictionary
rpsDict = dict({1:"Rock", 2:"Paper", 3:"Scissor"})

# print ruls of the game
start=input("Rules of \n1. Rock, \n2. Paper, \n3. Scissors. \nPress enter to continue.")
time.sleep(1)
print("\nRock wins against scissors")
print("\nPaper wins against rock")
print("\nScissors wins against paper")

# take user choice
computerchoice = random.randint(1,3)
userchoice=int(input("\n\nWhat do you choose? 1, 2, or 3?"))
print("OK, so you choose..."+rpsDict.get(userchoice) + "...smarty pants!")

# calculate computer choice with random selection
print("Now its my turn!")
time.sleep(0.6)
print("I choose...")
time.sleep(2)
print(rpsDict.get(computerchoice))

# decide the winner
if computerchoice == userchoice:
    print("That's a tie")
elif computerchoice - userchoice == 1:
    print("I win")
else:
    print("You win")

print("Thanks for playing!")
