import os
import sys
#text to speech
from gtts import gTTS

language = 'en'



def mytts(mytext, language):
    # language = 'en'
    ttsobj = gTTS(text=mytext, lang=language, slow=False)
    ttsobj.save("respond.mp3")
    os.system("mpg321 respond.mp3")
    os.system("rm respond.mp3")




#responces
not_understood = "Sorry, I don't recognize that."


#keywords from transcript (triggers)
start_task_triggers = ["firefox", "update", "upgrade", "shutdown", "reboot", "security", "scan"]
start_task_commands = ["firefox", "sudo apt update", "sudo apt upgrade -y", "shutdown", "reboot", "python3 ping2.py", "sudo python3 netscan.py -t 192.168.0.1/24"]

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
                    break
                else:
                    not_in += 1
                    continue
        except:
            print("sorry, I dont understand..")
            mytts(not_understood, "en")
            break
    
        







# messaging_task_triggers = []
# messaging_task_commands = []

    
