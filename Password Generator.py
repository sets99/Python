import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"
lengthofpasswords = int(input("How many characters?"))
print("\nHere are your passwords:")

password = ""
for x in range(lengthofpassword):
   password = password + random.choice(characters)

print (password)
