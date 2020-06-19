import time
seconds=int(input("How long of a timer? Answer in seconds \n"))
print ("Ok! I have set a timer for", seconds, " seconds")
print ("Start!")
time.sleep(seconds)
print("YOUR TIMER IS OVER!!!")
