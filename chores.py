import os
import sys
#text to speech
from gtts import gTTS



#network scan
from netscan import scan

language = 'en'



def mytts(mytext, language):
    # language = 'en'
    ttsobj = gTTS(text=mytext, lang=language, slow=False)
    ttsobj.save("respond.mp3")
    os.system("mpg321 respond.mp3")
    os.system("rm respond.mp3")




#responces
not_understood = "Sorry, I don't recognize that."

#misc
shut_up = "shut up hoe"

#keywords from transcript (triggers)
start_task_triggers = ["firefox", "update", "upgrade", "shutdown", "reboot", "security", "devices", "time", "internet", "weather", "remind"]
start_task_commands = ["firefox", "sudo apt update", "sudo apt upgrade -y", "shutdown", "reboot", "python3 ping2.py", "python3 netscan.py && python3 gen_email.py", "python3 time.py", "python3 is_online.py", "python3 scrapeweather.py", "python3 get_reminder.py && python3 timer.py"]


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
                    # if start_task_triggers[index] == "remind":
                    #     f = open("time.txt", "w")
                    #     f.write(str(words)
                    #     f.close()

                    os.system(start_task_commands[index])
                    break
                elif word not in start_task_triggers:
                    continue
                
                    
                else:
                    not_in += 1
                    # continue
        except:
            print("sorry, I dont understand..")
            mytts(not_understood, "en")
            break
    
        







# messaging_task_triggers = []
# messaging_task_commands = []

    
