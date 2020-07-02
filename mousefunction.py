import pyttsx3
import datetime
import time
import speech_recognition as sr
import pyautogui
import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.setProperty('volume',0.5)
engine.setProperty('rate', 155)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def downmouse():
    time.sleep(1)
    pyautogui.moveRel(0, 100, duration=0.1)

def rightmouse():
    time.sleep(1)
    pyautogui.moveRel(100, 0, duration=0.1)
def leftmouse():
    time.sleep(1)
    pyautogui.moveRel(-100,0,duration=0.1)
def upmouse():
    time.sleep(1)
    pyautogui.moveRel(0,-100,duration=0.1)
def rightclick():
    pyautogui.click(button='right')
def leftclick():
    pyautogui.click(button='left')
def takeCommand():
    # It takes microphone input from the usr and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source2:
        print("Listening...")
        r.adjust_for_ambient_noise(source2, duration=1)
        r.pause_threshold = 2

        audio = r.listen(source2)
        print("running")

    try:
        print("recognising...")
        querry = r.recognize_google(audio, language='en-in')
        print(f"User said : {querry}\n")
    except Exception as e:
        print("Say that again please...")
        return 'None'
    return querry
if __name__ == '__main__':
    while True:
        querry1 = list(takeCommand().split())
        # print(querry1)
        flag=False
        for i in querry1:
            # print(i)
            if i=="left":
                leftmouse()
            elif i=="right":
                rightmouse()
            elif i=="up":
                upmouse()
            elif i=="down":
                downmouse()
            elif i=="leftclick":
                leftclick()
            elif i=="rightclick":
                rightclick()
            elif i==("stop" or "exit" or "quit"):
                flag=True
                break
        if flag==True:
            break
