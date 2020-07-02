from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import getpass
import pyttsx3
import datetime
import speech_recognition as sr
import os
import time
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.setProperty('volume',0.5)
engine.setProperty('rate', 155)

#It speakes the commands
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
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

def send_message(target,string):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    # Replace username with your pc username(directory path of chrome data) 
    options.add_argument(r"--user-data-dir=C:\Users\{Username}\AppData\Local\Google\Chrome\User Data".format(getpass.getuser()))
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)
    target = f'"{target}"'
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
    print (group_title)
    print ("Wait for few seconds")
    group_title.click()
    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    message.send_keys(string)
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()
    driver.close()


if __name__ == '__main__':
    while True:
        speak("whom you want to send message")
        target=takeCommand()
        speak("tell me the message you want to send")
        string=takeCommand()
        send_message(target,string)
