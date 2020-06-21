date1=input("What is the date you want to measure from? Answer in the form: 5 \n")
date1=int(date1)
month1=input("What month number of the year you want to measure from? Answer in the form: 4 \n")
month1=int(month1)
year1=input("What year do you want to measure from? Answer in the form: 2020 \n")
year1=int(year1)
date2=input("What is the date you want to measure until? Answer in the form: 5 \n")
date2=int(date2)
month2=input("What is the month number of the year you want to measure until? Answer in the form: 4 \n")
month2=int(month2)
year2=input("What year do you want to measure until? Answer in the form: 2020 \n")
year2=int(year2) 
if year1 % 4 == 0:  
  if month1>month2 and date1>date2: 
    print ("That date is after...")
    print ( 32 - date1 + 1 + date2 - 1)
    print ("day(s)")
    print (12 - month1 + month2 - 1)
    print ("month(s)") 
    print (year2 - year1)
    print ("year(s)")

  if month1>month2 and date1==date2: 
    print ("That date is after...")
    print ("0")
    print ("day(s)")
    print (12 - month1 + month2 - 1)
    print ("month(s)")
    print (year2 - year1)
    print ("year(s)")
    
  if month1>month2 and date2>date1: 
    print ("That date is after...")
    print  (32 - date1 + 1 + date2 - 1)
    print ("day(s)")
    print (12 - month1 + month2 - 1)
    print ("month(s)")
    print (year2 - year1)
    print ("year(s)")




  if month2>month1 and date1>date2: 
    print ("That date is after...")
    print (month2 - month1)
    print ("month(s)")
    print (32 - date1 + 1 + date2 - 1)
    print (year2 - year1)
    print ("year(s)")
    
  if month2>month1 and date1==date2: 
    print ("That date is after...")
    print ("0")
    print ("day(s)")
    print (month2 - month1)
    print ("month(s)")
    print (year2 - year1)
    print ("year(s)")
  
  if month2>month1 and date2>date1:  
    print ("That date is after...")
    print (date2 - date1)
    print ("day(s)")
    print (month2 - month1)
    print ("month(s)")
    print (year2 - year1)
    print ("year(s)")
    
 
 
 
  if month2==month1 and date2==date1: 
    print ("That date is after...")
    print (date2 - date1)
    print ("day(s)")
    print (month2 - month1)
    print ("month(s)")
    print (year2 - year1)
    print ("year(s)")
  
    
   
        


else: 
   if month1>month2 and date1>date2: 
    print ("That date is after...")
    print  (31 - date1 + 1 + date2 - 1)
    print ("day(s)")
    print (12 - month1 + month2 - 1)
    print ("month(s)")
    print (year2 - year1)
    print ("year(s)")

   if month1>month2 and date1==date2: 
    print ("That date is after...")
    print ("0")
    print ("day(s)")
    print (12 - month1 + month2 - 1)
    print ("month(s)") 
    print (year2 - year1)
    print ("year(s)")
    
   if month1>month2 and date2>date1: 
    print ("That date is after...")
    print  (32 - date1 + 1 + date2 - 1)
    print ("day(s)")
    print (12 - month1 + month2 - 1)
    print ("month(s)") 
    print (year2 - year1)
    print ("year(s)")




   if month2>month1 and date1>date2: 
    print ("That date is after...")
    print (month2 - month1)
    print ("month(s)")
    print (32 - date1 + 1 + date2 - 1)
    print (year2 - year1)
    print ("year(s)")
    
   if month2>month1 and date1==date2: 
    print ("That date is after...")
    print ("0")
    print ("day(s)")
    print (month2 - month1)
    print ("month(s)")
    print (year2 - year1)
    print ("year(s)")
  
   if month2>month1 and date2>date1:  
    print ("That date is after...")
    print (date2 - date1)
    print ("day(s)")
    print (month2 - month1)
    print ("month(s)")
    print (year2 - year1)
    print ("year(s)")
