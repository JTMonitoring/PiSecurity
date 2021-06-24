from chores import mytts
from assistant import save_audio

mytts("what do you want me to remind you of, and when?", "en")

command = save_audio()
r = sr.Recognizer()

command_list = command.split(" ")

if "remind me to" in command:
    f = open("time.txt", "w")
    f.write(command)
    f.close()

