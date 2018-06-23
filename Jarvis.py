import speech_recognition as sr
import datetime
from time import ctime
import time
import os
import pyttsx
import webbrowser
import random
import requests
import cv2
import numpy as np

engine = pyttsx.init()


def speak(audioString):
    print(audioString)
    engine.say(audioString)
    engine.runAndWait()


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        data = ""
        try:
            data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print()
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def GMN():
    speak("Ok sir, Let's play guess my number")
    speak("This game is powered by voice!")
    speak("Please think of a number between 0 and 100!")
    high = 100
    low = 0
    x = ''
    while 'c' not in x:
        g = (high + low) // 2
        print("Is your secret number " + str(
            g) + "? Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter c to indicate I guessed correctly.")
        x = recordAudio()
        if "l" in x:
            low = int(g)
        elif "h" in x:
            high = int(g)
        elif 'c' in x:
            break
        else:
            speak("Sorry I did not understand your input.")
        int(g)
    speak("Game over. Your secret number was: " + str(g))

def jarvis(data):
    if "how are" in data:
        speak("fine sir")

    if "what time" in data:
        speak(ctime())

    if "Google" in data:
        speak("Ok Sir, I will now open google chrome.")
        ch = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
        os.system('"' + ch + '"')

    if "search the web" in data:
        d = data.split()
        lib = d[-1]
        speak("Ok, I will now search Google for " + lib)
        ur = ("https://www.google.com.sa/search?q=" + lib)
        webbrowser.open_new(ur)

    if "turn off" in data:
        speak("Yes sir")
        exit(1)

    if "game" in data:
        GMN()

    if "here" in data:
        speak("What should I say")
        l = recordAudio()
        for letter in l:
            speak(letter + "!")
        speak("What does that spell?")
        speak(l + "!!!!")

    if "Unity" in data:
        speak("Ok Sir, I will now open unity.")
        un = 'C:\\Program Files\\Unity\\Editor\\Unity.exe'
        os.system('"' + un + '"')

    if "python" in data:
        speak("Ok Sir, I will now open pycharm.")
        py = 'C:\\Program Files (x86)\\JetBrains\\PyCharm Community Edition 5.0.1\\bin\\pycharm.exe'
        os.system('"' + py + '"')

    if "VMware" in data:
        speak("Ok Sir, I will now open VMware.")
        ub = 'C:\\Program Files (x86)\\VMware\\VMware Player\\vmplayer.exe'
        os.system('"' + ub + '"')

    if "Java" in data:
        speak("Ok Sir, I will now open Java.")
        ec = 'C:\\Users\\ershada\\eclipse\\java-mars\\eclipse\\eclipse.exe'
        os.system('"' + ec + '"')

    if "Minecraft" in data:
        speak("Ok Sir, I will now open Minecraft.")
        mi = 'C:\\Program Files (x86)\\Minecraft\\MinecraftLauncher.exe'
        os.system('"' + mi + '"')

    if "camera studio" in data:
        speak("Ok Sir, I will now open Camstudio.")
        ca = 'C:\\Program Files\\CamStudio 2.7\\Recorder.exe'
        os.system('"' + ca + '"')

    if "hello" in data:
        speak("Hullo :)")

    if "info" in data:
        info_dict = {
            "telephone": {
                "Frank": "0541022183",
                "liver": "0541061737"
            },
            "email": {
                "Hotmail": {
                    "Oliver": "oliver.123@hotmail.com",
                    "Frank": "frank.123@hotmail.com"
                },
                "Gmail": {
                    "Oliver": "oliver.gmail.com",
                    "Frank": "frank.123@gmail.com",
                    "Elizabeth": "elizabeth.123@gmail.com"
                }
            }
        }
        speak("What would you like to know?")
        rec = recordAudio()
        if rec in info_dict:
            if "email" in rec:
                speak("Hotmail or Gmail?")
                hg = recordAudio()
                if "Hotmail" in hg:
                    speak("Who would you like to know this info about?")
                    person2 = recordAudio()
                    print(person2)
                    if person2 in info_dict['Hotmail']:
                        speak(info_dict['Hotmail'[person2]])
                        print(info_dict['Hotmail'[person2]])
                if "Gmail" in hg:
                    speak("Who would you like to know this info about?")
                    person2 = recordAudio()
                    print(person2)
                    if person2 in info_dict['Gmail']:
                        speak(info_dict['Gmail'[person2]])
                        print(info_dict['Gmail'[person2]])

            elif "telephone" in rec:
                speak("Who would you like to know this info about?")
                person = recordAudio()
                print(person)
                if person in rec:
                    speak(info_dict[rec[person]])
                    print(person)

    if "thank you" in data:
        speak("You're welcome")

    if "timer" in data:
        music = ["C:\Files\Arash\Python\Python_Projects\Music.ogg", "C:\Files\Arash\Python\Python_Projects\Music2.ogg"]
        if "minutes" in data:
            for i in data:
                if i.isdigit():
                    m = i
                    break
            speak("Turning timer on")
            speak("Note that when the timer is on I cannot answer to your commands")
            choice = random.randint(0, 1)
            try:
                mi = int(m)
            except:
                speak("I didn't understand that")
                exit()

            utc_now = datetime.datetime.utcnow()
            utc_then = utc_now + datetime.timedelta(minutes=mi)
            total = (utc_then - utc_now).total_seconds()
            speak("Turning Timer On for " + str(mi) + " minutes")
            time.sleep(total)
            speak("Turning Timer Off")
            os.system("start " + music[choice])

        if "second" in data:
            for i in data:
                if i.isdigit():
                    s = i
                    break
            speak("Turning timer on")
            speak("Note that when the timer is on I cannot answer to your commands")
            choice = random.randint(0,1)
            try:
                se = int(s)
            except:
                speak("I didn't understand that")
                exit(0)

            utc_now = datetime.datetime.utcnow()
            utc_then = utc_now + datetime.timedelta(seconds=se)
            total = (utc_then - utc_now).total_seconds()
            speak("Turning Timer On for " + str(se) + " seconds")
            time.sleep(int(total))
            speak("Turning Timer Off")
            os.system("start " + music[choice])
            print music[choice]

    if "weather" in data:
        speak("Searching...")
        import urllib2, urllib, json
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select wind from weather.forecast where woeid=2460286"
        yql_url = baseurl + urllib.urlencode({'q': yql_query}) + "&format=json"
        result = urllib2.urlopen(yql_url).read()
        data2 = json.loads(result)
        speak(data2['query']['results'])

    if "creator" in data:
        speak("My creator is TheVoyagerVibe")

    if "goodbye" in data:
        speak("Goodbye Sir")
        exit(1)

    if "see you later" in data:
        speak("I guess I'll see you later")
        exit(1)

    if "Alice" in data:
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[2].id)
        speak("Yes Sir?")

    if "Jarvis" in data:
        sound = engine.getProperty('voices')
        engine.setProperty('voice', sound[0].id)
        speak("Yes Sir?")

    if "music" in data:
        if "Ghost Rider" in data:
            os.system("start C:\Files\Arash\Python\Python_Projects\Music2.ogg")

        if "Unstoppable" in data:
            os.system("start C:\Files\Arash\Python\Python_Projects\Music.ogg")

    if "my name is" in data:
        data3 = data.split()
        speak("Oh, hi " + data3[-1])

    if "Bitcoin" in data:
        speak("Just a second...")
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        r = requests.get(url)
        speak("Bitcoin is $" + r.json()['bpi']['USD']['rate'])


# initialization
speak("Hello")
while 1:
    data = recordAudio()
    jarvis(data)
    speak(data)
