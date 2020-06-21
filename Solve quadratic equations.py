import math
import time
print ("Enter a,b,and c for your quadratic equation in the form: ax^2 + bx + c.")
time.sleep(1)
a=input("What is the value of a? \n")
b=input("What is the value of b? \n")
c=input("What is the value of c? \n")
a=float(a)
b=float(b)
c=float(c)
if a==0: 
  print ("What? That is not a quadratic equation! For it to be a quadratic, the variable A has to be greater than 0.")
else: 
  blahblahblah=b**2 - 4*a*c

if blahblahblah < 0:
  blahblahblah = blahblahblah * -1
  blahblahblahSQRT = math.sqrt(blahblahblah)
  realPart = (0-b)/(2*a)
  imaginaryPart = blahblahblahSQRT / (2*a)
  print(f'({realPart:f} + {imaginaryPart:f}i)')
  print(f'({realPart:f} - {imaginaryPart:f}i)')
  
else:  
  x1 = (0-b + math.sqrt(blahblahblah))/(2*a)
  x2 = (0-b - math.sqrt(blahblahblah))/(2*a)
  print ("The two solutions are...")
  print ({x1, x2})
