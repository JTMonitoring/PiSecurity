
import os
import sys
import time

from chores import mytts

time_measures = ["minutes", "hours", "seconds"]

def min_timer(minutes):

    return

def hour_timer(hours):
    return

def second_timer(seconds, reminder_name):
    print(seconds)
    sec = 0
    while True:
        
        sec +=1
        print(sec)
        time.sleep(1)
        if sec == int(seconds):
            mytts("Time to "+str(reminder_name), "en")
            break


f = open("time.txt", "r")
data = f.read()
f.close()

def timer():
    

    if "remind me" in data:
        data_list = data.split(" ")

        start_name = data_list.index("to")
        end_name = data_list.index("in")

        reminder_name = data_list[3:-3]

        for measurement in time_measures:
            if data_list[-1] == measurement:
                time_frame = measurement
        
        amount = ""
        amount = str(data_list[-2])

        


        if measurement == "seconds":
            outputstr = "I will remind you to "+str(reminder_name)+" in "+str(amount)+" "+time_frame
            print(outputstr)
            mytts(outputstr, "en")
            second_timer(amount, reminder_name)
        elif measurement == "minutes":
            outputstr = "I will remind you to "+str(reminder_name)+" in "+str(amount)+" "+time_frame
            print(outputstr)
            mytts(outputstr, "en")
            min_timer(amount, reminder_name)
        elif measurement == "hours":
            outputstr = "I will remind you to "+str(reminder_name)+" in "+str(amount)+" "+time_frame
            print(outputstr)
            mytts(outputstr, "en")
            hour_timer(amount, reminder_name)
        else:
            mytts("Sorry, I dont recognize that", "en")

def timer2():
    data_list = data.split(" ")
    if data_list[-1] == time_measures[0]:
        mytts("setting a timer for "+data_list[-2]+" "+data_list[-1], "en")
        min_timer(int(data_list[-2]))
    elif data_list[-1] == time_measures[1]:
        hour_timer(int(data_list[-2]))
    elif data_list[-1] == time_measures[2]:
        second_timer(int(data_list[-2]))
    



if "remind me" in data:
    timer1()
if "set a timer" in data:
    timer2()


            


#example string -- "remind me to x in y minutes" or "set a timer for x (time)"


        



