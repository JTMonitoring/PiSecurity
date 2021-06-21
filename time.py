from chores import mytts

import time
import os
import sys
from datetime import datetime

now = datetime.now()

military_hours = now.strftime("%H")
minutes = now.strftime("%M")

military_hours = military_hours.strip(":")
if int(military_hours) > 12:
    hour = int(military_hours) - 12
print(type(military_hours))

# print("Current Time =", current_time)
mytts("The time is "+str(hour)+" "+minutes, "en")


