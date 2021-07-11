import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



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
                cmd = cmd.replace('feona','')
    except:
        pass
    return cmd

def run_alexa():
    command =  takeCommand()
    print(command)
    if (command == ' exit'):
        return 'exit'
    #for playing something on youtube
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)
    
    # for time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') #format for pm for 24 hr ('%H:%M') 
        talk('time is '+time)
        print(time)
    
    elif 'tell me about' in command:
        srch = command.replace('tell me about','')
        ress = wikipedia.summary(srch,2)
        print(ress)
        talk(ress)
    
    elif 'joke' in command:
        jk = pyjokes.get_joke('en','all')
        print(jk)
        talk(jk) 
    

    else:
        print('please say a command')
        
while True:
    run_alexa()
    if run_alexa() == 'exit':
        break