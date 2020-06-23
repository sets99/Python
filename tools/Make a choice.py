import random

print ("Have trouble making a choice? Don't worry we can help you out.")
print("\n")

numberofitems=int(input("How many options do you have?"))
print("OK, enter your choices now one by one and hit enter")

listItems = []

for x in range (numberofitems):
  listItems.append(input(""))

chosenItem = random.choice(listItems)
print("I think that you should go with: " + chosenItem)
