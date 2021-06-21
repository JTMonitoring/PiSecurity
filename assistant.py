import speech_recognition as sr
import os.path
from os import path
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub import AudioSegment
from pydub.playback import play
import time

#text to speech
from gtts import gTTS

from chores import *

r = sr.Recognizer()


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
        
        trigger = "assistant"
        sudo_trigger = "sudo penis"
        chore = save_audio()
        if trigger in chore:
            # voice = AudioSegment.from_mp3('src/library/greeting.mp3')
            # play(voice)
            mytts("How can I help?", "en")
            # chore.executechore(chore)
            # insult(chore)
            try:
                transcript = save_audio()
                think(transcript)
            except:
                noaudio = True


    except:
        noaudio = True
        



                
