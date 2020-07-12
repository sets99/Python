import random
import time

file = open("wordlist.txt", "r")

if file.mode == "r": 
  read = file.readlines()

word = random.choice(read).rstrip()

#word = "me"

name=input("Hi! What's your name?")
time.sleep(0.5)
print("Well, " + name + ", Time to play hangman!")
time.sleep(1.3)


print("Ok! I've chosen a %d letter word." %(len(word)))

tracker = []
dict = {}

for i in range(0, len(word)):
  dict[word[i]] = []

for i in range(0, len(word)):
  tracker.append("___")
  dict[word[i]].append(i)


for x in range(30): 
  print(' '.join(tracker) + "\n")
  guess = input("Guess a letter.")
  if guess in word:
    print("\nGood Job!")
    position = dict.pop(guess)
    tracker[position] = guess
    if len(dict) == 0: 
      print("You won! The word was " + word)
      break
    
  else: 
    print("\nTry again")
  
else: 
  print("You lost... The word was " + word + ".") 
 
