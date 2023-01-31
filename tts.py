import speech_recognition as sr
from gtts import gTTS
import playsound
import os

def speak(text):
     tts = gTTS(text=text, lang='ko')
     filename='voice.mp3'
     tts.save(filename)
     playsound.playsound(filename)
     os.remove('voice.mp3')
