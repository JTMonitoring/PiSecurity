import os
import sys

#keywords from transcript (triggers)
start_task_triggers = ["firefox", "update", "upgrade", "shutdown", "reboot", "security"]
start_task_commands = ["firefox", "sudo apt update", "sudo apt upgrade -y", "shutdown", "reboot", "python3 ping2.py", "nothing"]

#security triggers/commands:
security_task_triggers = ["start security", "disable security", "read log"]
security_task_commands = ["cd ~/security && ./startall", "cd ~/security && ./stopall", "cd ~/security && python3 readlog.py"]

def think(transcript):
    print("thinking.. "+transcript)
    print("TEST")
    print(type(transcript))
    words = transcript.split(" ")
    print(type(words))
    print(words)
    
   

    for word in words:
        word = word.lower()
        print(word)
        try:            
            for trigger in start_task_triggers:
                # print("Trigger: "+trigger)
                
                if word in start_task_triggers:
                    index = start_task_triggers.index(word)
                
            print(start_task_commands[index])
            os.system(start_task_commands[index])
                
        except:
            print("sorry, I dont understand..")
    
        







# messaging_task_triggers = []
# messaging_task_commands = []

    