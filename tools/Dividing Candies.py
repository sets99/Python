import random
import math
number_of_candies=int(input("How many candies? "))
if number_of_candies<=0:
	print("No jokes please. Be serious. ")
	exit()
#Number of candies
number_of_kids=int(input("How many people? "))
#Number of kids
number_of_candies_for_each_kid=math.floor(number_of_candies/number_of_kids)
remaining_candies=number_of_candies - (number_of_candies_for_each_kid*number_of_kids)

print("You can give " + str(number_of_candies_for_each_kid) + " to each person and keep " + str(remaining_candies) + " candies to yourself. ")
