import random

print('Welcome to your password generator')

numberofcharacters = input('\nHow many characters do you want in your password? Choose from 3 to 10')
numberofcharacters = int(numberofcharacters)

listofletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

LETTER1 = random.choices(listofletters)
NUMBER1 = random.randint(0,9)
LETTER2 = random.choices(listofletters)
NUMBER2 = random.randint(0,9)
LETTER3 = random.choices(listofletters)
NUMBER3 = random.randint(0,9)
LETTER4 = random.choices(listofletters)
NUMBER4 = random.randint(0,9)
LETTER5 = random.choices(listofletters)
NUMBER5 = random.randint(0,9)
LETTER6 = random.choices(listofletters)
NUMBER6 = random.randint(0,9)
LETTER7 = random.choices(listofletters)
NUMBER7 = random.randint(0,9)
LETTER8 = random.choices(listofletters)
NUMBER8 = random.randint(0,9)
LETTER8 = random.choices(listofletters)
NUMBER8 = random.randint(0,9)
LETTER8 = random.choices(listofletters)
NUMBER8 = random.randint(0,9)
LETTER9 = random.choices(listofletters)
NUMBER9 = random.randint(0,9)
LETTER10 = random.choices(listofletters) 
NUMBER10 = random.randint(0,9)

letterlist = [LETTER1, LETTER2, LETTER3, LETTER4, LETTER5, LETTER6, LETTER7, LETTER8, LETTER9, LETTER10]
numberlist = [NUMBER1, NUMBER2, NUMBER3, NUMBER4, NUMBER5, NUMBER6, NUMBER7, NUMBER8, NUMBER9, NUMBER10]

randomletter = random.choice(letterlist)
randomnumber = random.choice(numberlist)

if numberofcharacters == "3": 
  print(f'{randomletter} + {randomnumber}')
  
  
