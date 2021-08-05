import os
import pyglet
from gtts import gTTS
from time import sleep

def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    sleep(music.duration)
    os.remove(filename) 

