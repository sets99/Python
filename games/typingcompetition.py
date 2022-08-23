import random
import time
import Levenshtein

sentences=[
'Hello, how are you doing today?',
'The cow is eating the grass in the lawn.',
'Jack and Jill are playing tennis, but they played badminton yesterday.',
'Is it time for lunch yet?',
'The weather is amazing today!'
]


num_players = int(input("How many players are playing?"))

cpm_dict={}

for x in range(1, num_players+1):
    player_name = input("What is the %dth player name?" %x)
    randnum = random.randint(1,len(sentences))
    sentence = sentences[randnum]
    characters = sentence.split()
    print("Type the following sentence and fast and as accurately as you can.")
    time.sleep(1)
    print("\n")
    start=time.time()
    entered_sentence = input(sentence)
    entered_characters = entered_sentence.split()
    end=time.time()
    elapsed_time=(end-start)
  
    
            
    ccpm = (len(entered_characters) - Levenshtein.distance(sentence,entered_sentence))/(elapsed_time)
    cpm_dict[player_name]=ccpm




print("The game is complete!")
winner = max(cpm_dict, key=cpm_dict.get)
print("The winner is...")
print("3")
time.sleep(2)
print("2")
time.sleep(2)
print("1")
time.sleep(2)
print("%s!" %winner)
