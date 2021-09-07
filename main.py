import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia as wiki

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# engine.say("I am Alexa. What can I do for you?")
# engine.runAndWait()

def alexaToYou(text):
    engine.say(text)
    engine.runAndWait()

def youToAlexa():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            alexaToYou("say a command")
            command = sr.Recognizer().recognize_google(sr.Recognizer().listen(source))
    except:
        pass
    print(command)
    return command

def run_alexa():
    srch_wrds = {"subject" : ["who is ", "what is ", "tell me something about ", "do you know "],
                 "av":["play ", "i want to listen to ", "i want to watch "],
                 "time":["what time is it ", "what time is now "]}
    command = youToAlexa()
    if any(x in command for x in srch_wrds["av"]):
        to_play = command.split("play ")[-1]
        alexaToYou("Playing" + to_play)
        pywhatkit.playonyt(to_play)
    elif any(x in command for x in srch_wrds["time"]):
        time = datetime.datetime.now().strftime('%I:%M %p')
        alexaToYou("The time is "+ time)
        print("The Time is " + time)
    elif any(x in command for x in srch_wrds["subject"]):
        subject = command.split("who is ")[-1]
        summary = wiki.summary(subject,1)
        print(summary)
        alexaToYou(summary)
    else:
        alexaToYou("Command not understood")
        run_alexa()


run_alexa()

#pywhatkit.sendwhatmsg(f"+919952098168", "Love you Phekku - This is python automated message",3,8)