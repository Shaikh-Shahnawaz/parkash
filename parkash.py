import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import json
import requests
from tkinter import *
from random import randint

# api key e6419180e9f944c99e23344f423c28d9


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(Audio):
    engine.say(Audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 6:
        speak('good night saad')
    elif hour >= 6 and hour <= 12:
        speak('good morning saad !')
    elif hour >= 12 and hour <= 15:
        speak('good afternoon saad !')
    elif hour >= 15:
        speak('good evening saad')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        print('listeing...!')
        r.pause_threshold = 1
        audio = r.listen(Source)

    try:
        print('recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user say:{query}")
        # speak(query)
    except Exception as e:
        # print(e)
        speak("I can't understand ")
        return 'none'
    return query

def news():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=efa0ddd8997f417fa23a08f8ee62633b"
    news = requests.get(url).text

    print(news["articles"])
    # head = news["articles"]
    for i in range(0, 5):
        if i < 4:
            speak(news["articles"][i]["title"])
            print(news["articles"][i]["title"])


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saadchaudhary646@gmail.com', '65%Saadd.')
    server.sendmail('saadchaudhary646@gmail.com', to, content)
    server.close()


def rolldices():
    R = randint(1, 6)
    if R == 1:
        print("you get one")
        speak("you get one")
    elif R == 2:
        print("you get two")
        speak("you get two")
    elif R == 3:
        print("you get three")
        speak("you get three")
    elif R == 4:
        print("you get four")
        speak("you get four")
    elif R == 5:
        print("you get five")
        speak("you get five")
    elif R == 6:
        print("you get six")
        speak("you get six")


if __name__ == "__main__":
    wishme()
    # speak('arfaan mera babu hai lalalalalalal')
    while True:
        query = takecommand().lower()
        # every logic possiable
        if 'wikipedia' in query:
            print('searching on wikipedia...')
            speak('searching on wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'who created you' in query:
            speak('i am created by developer name saad chaudhary')

        elif 'who are you' in query:
            speak('I am parkash')

        elif 'what is your goal' in query:
            speak('My goal is to take world in next level of automation')
        elif "news " in query:
            news()

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            music_dir = 'E:\\soong'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[0]))
        elif 'open sublime' in query:
            code = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(code)
        elif 'tell time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir ,Its {time}")
        elif 'roll a dice' in query:
            rolldices()
        elif 'send email' in query:
            try:
                speak('what should i write')
                content = takecommand()
                to = 'saadchaudhary646@gmail.com'
                sendemail(to, content)
                speak('sir email has been send')
            except Exception as e:
                print(e)
                speak('sir! i am NOT  able to access')

#
# root = Tk()
# root.title("Parkash")
# menu = Menu(root)
# root.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="New")
# filemenu.add_command(label="Open...")
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.quit)
#
# helpmenu = Menu(menu)
# menu.add_cascade(label="Help", menu=helpmenu)
# helpmenu.add_command(label="About...")


#
# back = Frame(root,bg='black')
# back.pack(fill="both")
# l=Label(back,text="cliick on button to interact with parkash",bg="orange")
# l.pack(fill="both")
# w = Button(back,text="on")
# w.bind("<Button-1>",hello)
# w.pack()
# b= Button(back,text="greet")
# b.bind("<Button-1>",wishme)
# b.pack()
# ll= Button(back,text="stop")
# ll.bind("<Button-1>",root.quit)
# ll.pack()
#
# root.mainloop()
