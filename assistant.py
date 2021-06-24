import speech_recognition as sr
import os.path
from os import path
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub import AudioSegment
from pydub.playback import play
import time
import urllib.request

from pythonping import ping

#text to speech
from gtts import gTTS

from chores import *

r = sr.Recognizer()



def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        mytts("no Internet", "en")

        



def save_audio():
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=6)
        print("listening...")
        text = r.recognize_google(audio_data)
        
    # print(text)
    return text
while True:
   
    try:    
        # transcript = save_audio()
        # print("[INPUT RECIEVED]:", transcript)
        connect()
        trigger = "assistant"
        
        sudo_trigger = "sudo penis"
        chore = save_audio()
        if trigger in chore:
            # voice = AudioSegment.from_mp3('src/library/greeting.mp3')
            # play(voice)
            mytts("How can I help?", "en")
            os.system("mpg123 src/library/start.wav")
            # chore.executechore(chore)
            # insult(chore)
            try:
                transcript = save_audio()
                think(transcript)
            except:
                noaudio = True


    except:
        noaudio = True
        



                
