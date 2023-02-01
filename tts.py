from gtts import gTTS
import pygame
import os

def speak(text):
     tts = gTTS(text=text, lang='ko')
     filename='voice.mp3'
     tts.save(filename)
     pygame.mixer.init()
     pygame.mixer.music.load("voice.mp3")
     pygame.mixer.music.play()
     while pygame.mixer.music.get_busy() == True:
          continue     
     os.remove('voice.mp3')

