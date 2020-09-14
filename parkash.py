import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from pygame import mixer
import requests
from random import randint
import tkinter as tk
from tkinter import ttk
from tkinter import *


AZLL=[]

def sdwqdkf(i):
    print(AZLL)
    AZLL.append(i)
    return AZLL[-1]


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

def textrere(a):
    return a

def liat(i):
    return AZLL.append(i)


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
        # print("you get one")
        speak("you get one")
    elif R == 2:
        # print("you get two")
        speak("you get two")
    elif R == 3:
        # print("you get three")
        speak("you get three")
    elif R == 4:
        # print("you get four")
        speak("you get four")
    elif R == 5:
        # print("you get five")
        speak("you get five")
    elif R == 6:
        # print("you get six")
        speak("you get six")



def callback(url):
    webbrowser.open_new(url)


if __name__ == '__main__':

    root = Tk()

    def btnClickFunction():
        nl = '\n'
        picture_file.insert('end',f' {nl} {AZLL[-1]}')


    # This is the section of code which creates the main window
    root.geometry('520x380')
    root.configure(background='#2e354f')
    root.title('Hello, I\'m the main window')


    # First, we create a canvas to put the picture on

    worthAThousandWords= tk.Frame(root,height=250, width=250)
    picture_file =Text(worthAThousandWords,height=15,width=30)
    picture_file.pack(fill=BOTH, side=LEFT, expand=True)
    # picture_file.insert('end', textrere())
    picture_file.focus_set()


    worthAThousandWords.place(x=25, y=82)


    def buttonClick():

        r = sr.Recognizer()
        with sr.Microphone() as Source:
            print('listeing...!')
            r.pause_threshold = 0.7
            r.energy_threshold = 400
            audio = r.listen(Source)

        try:
            print('recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"user say:{query}")
            speak(query)
        except Exception as e:
            print(e)
            speak("I can't understand ")
            return 'none'

        query.lower()
        if 'wikipedia' in query:
            print('ajksnfjnfwfweofwjo')
            speak('searching on wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            # print(result)
            speak(result)
            # liat(result)

        elif 'who created you' in query:
            speak('i am created by developer name saad chaudhary')
            liat('i am created by developer name saad chaudhary')


        elif 'who are you' in query:
            speak('I am parkash')
            # btnClickFunction()

        elif 'what is your goal' in query:
            speak('My goal is to take world in next level of automation')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            music_dir = 'E:\\soong'
            song = os.listdir(music_dir)
            # print(song)
            os.startfile(os.path.join(music_dir, song[0]))
        elif 'open sublime' in query:
            code = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(code)
        elif 'show time' in query:
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
                # print(e)
                speak('sir! i am NOT  able to access')




    MyButton6 = Button(root, command=buttonClick, bd=0, activebackground='#c1bfbf', overrelief='groove')

    MyButton6.pack()
    # This is the section of code which creates the a label
    Label(root, text='Hello how may i help you ??',fg='#f0593a', bg='#2e354f', font=('arial', 30, 'normal')).place(x=10, y=22)


    # This is the section of code which creates a button
    w=Button(root, text='Button mic!', bg='#f0593a', font=('arial', 20, 'normal'),command=btnClickFunction)
    # w.bind("<Button-1>",hello)

    w.place(x=305, y=262)


    # This is the section of code which creates a text input box
    tInputss=Entry(root)
    tInputss.place(x=325, y=92)

    # This is the section of code which creates a footer bar
    footer = tk.Frame(root, bg='#f0593a', height=30)
    link1 = Label(footer, text="design and develop by chaudhary saad ,mirza arham", fg="black",bg='#f0593a', cursor="hand2",)
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://hyperdec.com/"))
    footer.pack(fill='both',side='bottom')



    root.mainloop()







