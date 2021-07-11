import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime


listner = sr.Recognizer()
engine = pyttsx3.init()

#change voices
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[10].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

#for machine to say
def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as sc:
            print("Listening......")
            vc = listner.listen(sc)
            cmd = listner.recognize_google(vc)
            cmd = cmd.lower()
            if 'alexa' in cmd:
                cmd = cmd.replace('alexa','')
    except:
        pass
    return cmd

def run_alexa():
    command =  takeCommand()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('time is '+time)
        print(time)

run_alexa()