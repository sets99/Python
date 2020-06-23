import time
import random

while True:
  topic = input('''What math skill would you like to work on today?
\nAddition, Subtraction, Multiplication, or division?''')
  print("Type STOP when you want to exit the current topic and move on to another one.")
  time.sleep(0.8)

  if topic.lower() == "addition":
    while True:
      number1=random.randint(1,100)
      number2=random.randint(1,100)
      answer=input("What is " + str(number1) + '+' + str(number2) + '?') 
      if answer == str(number1 + number2): 
          print("\nCorrect! Great Job!")
      elif answer.upper() == "STOP":
        break
      else: 
        print("\nNope! The correct answer is " + str(number1 + number2) + '.')
        

  if topic.lower() == "subtraction":
    while True:
      number1=random.randint(1,100)
      number2=random.randint(1,100)
      answer=input("What is " + str(number1) + '-' + str(number2) + '?') 
      if answer == str(number1 - number2): 
        print("\nCorrect! Great Job!")
      elif answer.upper() == "STOP":
        break
      else: 
        print("\nNope! The correct answer is " + str(number1 - number2) + '.')



  if topic.lower() == "multiplication": 
    while True: 
      number1=random.randint(1,100)
      number2=random.randint(1,100)
      answer=input("What is " + str(number1) + ' X ' + str(number2) + '?') 
      if answer == str(number1 * number2): 
        print("\nCorrect! Great Job!")
      elif answer.upper() == "STOP":
        break
      else: 
        print("\nNope! The correct answer is " + str(number1 * number2) + '.')
    


  if topic.lower() == "division": 
    while True: 
      number1=random.randint(1,10)
      number2=random.randint(1,10)
      multiply = number1*number2
      useranswer = input("What is " + str(multiply) + "/" + str(number1) + " ?")
      if useranswer.upper() == "STOP":
        break
      elif int(useranswer) == number2: 
        print("\nCorrect! Great Job!")
      else: 
        print("\nNope! The correct answer is " + str(number2) + ".")
  
      
      
