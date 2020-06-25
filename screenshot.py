import pyttsx3
import datetime
import speech_recognition as sr
import os
import pyautogui
import time
import random
import pyaudio
# import Pillow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.setProperty('volume',0.5)
engine.setProperty('rate', 155)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takescreenshot():
    screenshot=pyautogui.screenshot()
    folder="./screenshot/"
    if not os.path.exists(folder):
        os.makedirs(folder)
    while True:
        r = random.randint(1, 100)
        l=[0]
        for filename in os.listdir(folder):
            new_name = os.path.splitext(filename)[0]
            l.append(int(new_name))
        next=max(l)+1
        screenshot.save(f'{folder}{next}.png')
        break
    speak('screen captured')

if __name__ == '__main__':
    takescreenshot()


