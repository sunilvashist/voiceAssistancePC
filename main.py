import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib
from youtube_search import YoutubeSearch
import pyaudio


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# engine.setProperty('volume',0.5) 
engine.setProperty('rate', 155) 



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening ")
    
    speak("I am Jarvis , how may I help you ")


def takeCommand():
    #It takes microphone input from the usr and return string output

    r=sr.Recognizer()
    with sr.Microphone() as source2:
        print("Listening...")
        r.adjust_for_ambient_noise(source2, duration=1 )
        r.pause_threshold=2

        audio= r.listen(source2)
        print("running")


    try:
        print("recognising...")
        querry=r.recognize_google(audio,language='en-in')
        print(f"User said : {querry}\n")
    except Exception as e:
        print("Say that again please...")
        return 'None'
    return querry

def sendmail(to, message):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('vaibhawtesing@gmail.com','Vaibhaw@123')
    server.sendmail('vaibhawtesting@gmail.com',to, message)
    server.close()



    

if __name__=='__main__':
    # speak('You are the best ! ')
    # print("Hello world !")
    wishMe()
    while True:
        querry=takeCommand().lower()

        if 'wikipedia' in querry:
            speak('Searching wikipedia')
            querry=querry.replace('wikipedia',"")
            results=wikipedia.summary(querry,sentence=2)
            print("According o wikipedia ")
            speak("According o wikipedia ")
            print(results)
            speak(results)
        elif 'play music' in querry:
            music_dir='C:\\Vaibhaw\\Development\\Jarvis\\music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in querry:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in querry:
            code_path="C:\\Users\\vaibh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('Opening Visual Studio Code')
            os.startfile(code_path)
        elif 'open pycharm' in querry:
            code_path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3\\bin\\pycharm64.exe"
            speak("Opening Pycharm ")
            os.startfile(code_path)
        elif 'open google' in querry:
            speak("Opening google.com")
            webbrowser.open("www.google.com")
        elif  'open youtube' in querry:
            speak("Opening youtube.com")
            webbrowser.open(("www.youtube.com"))
        elif  'send mail' in querry:
            try:
                speak("Please say the Recipient email address ")
                to=takeCommand()
                speak("Please dictate the message to send ")
                message=takeCommand()
                sendmail(to,message)
                speak("Email has been sent")
            except Exception as e:
                # print(e)
                speak("e-mail didn't sent due to "+str(e))
        elif 'open whatsapp' in querry:
            speak("Opening whatsapp")
            webbrowser.open(("https://web.whatsapp.com/"))
        elif 'search' in querry and 'youtube' in querry:
            results=querry.replace("search","").replace("youtube","").replace("on","")
            speak("opening "+YoutubeSearch(results,max_results=2).to_dict()[0]['title'])
            webbrowser.open(url="www.youtube.com"+YoutubeSearch(results,max_results=5).to_dict()[0]['link']+' in youtube')
        elif 'search' in querry and 'google' in querry:
            results=querry.replace('search',"").replace('google','')
            speak('Opening '+results+" in google ")
            webbrowser.open('http://google.com/?#q'+results)
        elif 'shut down' in querry or 'power off' in querry or 'shutdown' in querry:
            speak("Want to shutdown your computer ? (yes or no): ");
            command=takeCommand()
            if 'yes' in command:
                speak('Shuting down computer in 10 seconds')
                for i in range(10,0,-1):
                    speak(i+1)
                os.system("shutdown /s /t 1");
                print("Shut down")
        elif 'open' in querry and 'chess' in querry or 'game' in querry:
            os.startfile('C:\\Program Files\\Microsoft Games\\Chess\\chess.exe')
            speak('Opening chess ')

        elif 'tell' in querry and 'joke' in querry:
            speak("Why was 6 afraid of 7?")
            print("Why was 6 afraid of 7 ?")
            ans=takeCommand()
            if ans=='7 8 9':
                speak('Ha ha ha')
            else:
                speak(" because ... 7 .... ate.........  9 ")
                print(" because ... 7 .... ate.........  9 ")
        elif 'date with me' in querry:
            speak("Excuse......... me !, I'm not your girl friend. We are just friends ") 
        
        elif  'cook' in querry and 'for' and 'me' in querry:
            speak("I'm so sorry , I'm just a robot and you haven't feeded cooking skill into memory, but I think you are a better cook than me and you'll make it more tastey meal, why don't you give a try ? ")


        elif 'quit' in querry or 'exit' in querry or 'stop'in querry:
            speak('Jarvis shutting down...')
            break

        
            

            
