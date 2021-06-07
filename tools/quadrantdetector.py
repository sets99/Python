x = float(input("insert x coordinate: "))
y = float(input("insert y coordinate: "))

if x>0 and y>0:
  print("First quadrant")
  
if x<0 and y>0: 
  print("Second quadrant")
  
if x<0 and y<0: 
  print("Third quadrant")
  
if x>0 and y<0: 
  print("Fourth quadrant")
