import random
print ("Tell me your two options and I will tell you which one to do.") 
a=input("What is your first option? \n")
b=input("What is your second option? \n")
listOfChoices = [a, b]
choice = random.choice(listOfChoices)
reply = ("Go for ") + choice
print (reply)
