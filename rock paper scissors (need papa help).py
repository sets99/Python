import random
import time
start=input("Rules of \n1. Rock, \n2. Paper, \n3. Scissors. \nPress enter to continue.")
time.sleep(1)
print("\nRock wins against scissors")
print("\nPaper wins against rock")
print("\nScissors wins against paper")
computerchoice = random.randint(1,3)
userchoice=input("\n\nWhat do you choose? 1, 2, or 3?")
print("Now its my turn!")
time.sleep(0.6)
print("I choose...")
time.sleep(2)
print(computerchoice)
if computerchoice == 1: 
  computerchoicename = "Rock"
if computerchoice == 2: 
  computerchoicename = "Paper"
if computerchoice == 3: 
  computerchoicename = "Scissors"
if (computerchoice == 1 and userchoice == 2) or (computerchoice == 2 and userchoice == 1): 
  print("I chose " + computerchoicename + ", " + "while you chose " + userchoice + ". " + "Paper wins!")
  
if (computerchoice == 1 and userchoice == 3) or (computerchoice == 3 and userchoice == 1): 
  print("I chose " + computerchoicename + ", " + "while you chose " + userchoice + ". " + "Rock wins!")
  
if (computerchoice == 2 and userchoice == 3) or (computerchoice == 3 and userchoice == 2): 
  print("I chose " + computerchoicename + ", " + "while you chose " + userchoice + ". " + "Scissors wins!")
if computerchoice == userchoice: 
  print("I chose " + computerchoicename + ", " + "while you chose " + userchoice + ". " + "That one was a tie...")
