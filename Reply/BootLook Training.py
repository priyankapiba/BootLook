import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pytest

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

    
def talk(text):
    engine.say(text)
    #engine.say('What can I do for you?')
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            #print("Listening....")
            talk('Listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bhoot look' in command:
                command = command.replace('bhoot look','')
                print(command)
    except:
        pass
    return command

def run_bot():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('Playing' + song)
        pywhatkit.playonyt(song)


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')    #I is 12hrs format and H is 24hr format and p is for "am" or "pm"
        talk('Current time is ' + time)

    elif 'who' in command: 
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        talk(info)
    
    elif 'what' in command:
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing,1)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'bye' in command:
        talk('bye')
        exit()

    else:
        talk('Please say it again?')
talk('Hey, I am Bootlook')
while True:
    talk('How can I help you?')
    
    run_bot()
