#import time for realistic effect
import time

#asking the two dates
print("Tell me two dates, and I will tell you how much time later is the second date than the first one.")
date1=int(input("What is the date number you want to measure from? Answer in the form: 18\n"))
month1 = int(input("\nWhat is the month number you want to measure from? Answer in the form: 3\n"))
year1 = int(input("\nWhat is the year number you want to measure from? Answer in the form: 2022\n"))
date2=int(input("What is the date number you want to measure until? Answer in the form: 7\n"))
month2 = int(input("\nWhat is the month number you want to measure until? Answer in the form: 4\n"))
year2 = int(input("\nWhat is the year number you want to measure until? Answer in the form: 2021\n"))

#defining a dictionary for months
MonthDict = dict({1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"})

