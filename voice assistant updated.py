import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyttsx3
import os
import smtplib
import requests
import json
import pywhatkit as kit
from pygame import mixer as mix
import time
import pyjokes

l1 = {"rohit": "rt8tyagi4366@gmail.com", "naksh": "freefund73@gmail.com",
      "shubham": "ss515312@gmail.com", "johny sins": "8bptyagi4366@gmail.com", "vikas": "vikasofficial911@gmail.com"}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("rate", 130)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def news(query):
    for i in range(5):
        r = requests.get(
            f'https://newsapi.org/v2/top-headlines?country=in&category={query}&apiKey=8f7d5117310f420cac0cd3b537554ec6')
        data = json.loads(r.content)
        print(f"News {i + 1} =>{data['articles'][i]['title']}\n")
        print(f"{data['articles'][i]['description']}\n")
        print(f"URl for the News is :-{data['articles'][0]['url']}\n")
        print(f"{data['articles'][i]['content']}\n")
        num = (data['articles'][i]['content'])
        speak(num)


def greet():
    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        speak("good morning sir")
    elif 13 < hour < 20:
        speak("good evening sir")
    else:
        speak("good evening  sir")
    speak("i am nakshatra how may i help you")


def takecommand():
    # it takes microphone input from user and return txt output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognising...")
            query = r.recognize_google(audio, language='en-in')
            print(f"input by user => {query.capitalize()}")
        except Exception as e:
            print("say that again please")
            return "None"
        return query


def email_input():
    # it takes microphone input from user and return txt output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("speak the content you want to send through email")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognising...")
            query = r.recognize_google(audio, language='en-in')
            print(f"content to be sent => {query.capitalize()}")
        except Exception as e:
            print("say that again please")
            return "None"
        return query


def set_reminder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("sir kindly speak, what reminder you want to set")
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("setting reminder....")
            speak("reminder has been successfully set in test.txt file")
            hello = r.recognize_google(audio, language='en-in')
        except Exception as e:
            print("say that again please")
            return "None"
        return hello


def send_email(email_name):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login('rt2tyagi4366@gmail.com', '11101999tyagi')
    msg = email_input()
    s.sendmail("rt2tyagi4366@gmail.com", email_name, msg)
    s.quit()


if __name__ == '__main__':
    greet()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("searching in wikipedia")
            query = query.replace("wikipedia", "")
            answer = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(answer)
            speak(answer)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak(" what do you want to search on google")
            query = takecommand().lower()
            kit.search(query)

        elif 'open facebook' in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            speak("which song you want to listen ?")
            query = takecommand()
            kit.playonyt(query)

        elif 'the time' in query:
            time = datetime.datetime.now().time()
            print(time)
            speak(time)

        elif 'the date' in query:
            date = datetime.datetime.now().date()
            print(date)
            speak(date)

        elif 'open  google chrome' in query:
            chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            speak("opening google chrome")
            os.startfile(chrome_path)

        elif 'hello david' in query:
            speak("hello sir i am vary good , i hope you are doing great, have a great day")

        elif 'set reminder' in query:
            reminder_text = set_reminder()
            f = open("test.txt", "w")
            f.write(reminder_text)
            f.close()

        elif 'what are my' in query:
            f = open("test.txt", "r")
            read = f.read()
            speak(read)
            print(read)

        elif 'send email' in query:
            speak("to whom you want to send email")
            query = takecommand().lower()
            if 'nakshatra' in query:
                name = "nakshatra"
                query = "freefund73@gmail.com"
            elif 'shubham' in query:
                name = "shubham"
                query = "ss515312@gmail.com"
            elif 'vikas' in query:
                name = "vikas"
                query = "vikasofficial911@gmail.com"

            elif 'rohit' in query:
                name = "rohit"
                query = "rt8tyagi4366@gmail.com"
            elif 'johnny sins' in query:
                name = "johnny sins"
                query = "8bptyagi4366@gmail.com"
            else:
                speak("cannot recognise the user")
                break
            speak(f"sending email to {query}...")
            send_email(query)
            speak(f"email sent  successfully")

        elif 'news' in query:
            speak("what category of news you want to listen?")
            query = takecommand().lower()
            if 'business' in query:
                query = "business"
            elif 'technology' in query:
                query = "technology"
            elif 'entertainment' in query:
                query = "entertainment"
            elif 'science' in query:
                query = "science"
            else:
                speak("cannot specify the category")
            news(query)

        elif 'shutdown' in query:
            speak("bye boss have a good day")
            exit()

        elif 'search for me' in query:
            query = takecommand().lower()
            inf = kit.info(query, return_value=True)
            speak(inf)

        elif 'open notepad' in query:
            speak("opening notepad")
            path = 'C:\\WINDOWS\\system32\\notepad.exe'
            os.startfile(path)

        elif 'open task manager' in query:
            speak("opening task manager")
            path = 'C:\\WINDOWS\\system32\\Taskmgr.exe'
            os.startfile(path)

        elif 'minute alarm' in query:
            speak(
                f"at what minute you want to buzz the alarm. current time in minutes is {datetime.datetime.now().minute}")
            query = int(takecommand())

            speak("alarm has been set successfully")
            if query > 60:
                speak("unable to set alarm")
                break
            else:
                while True:
                    tim = int(datetime.datetime.now().minute)
                    if query == tim:
                        mix.music.play()
                        time.sleep(10)
                        mix.music.stop()

        elif 'a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)


        else:
            print("--------------------->")
