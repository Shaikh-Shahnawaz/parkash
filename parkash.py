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
from PIL import  ImageTk, Image
from random import randint



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(Audio):
    engine.say(Audio)
    engine.runAndWait()


def wishme(events):
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
        # print('listeing...!')
        r.pause_threshold = 1
        audio = r.listen(Source)

    try:
        # print('recognizing...')
        query = r.recognize_google(audio, language='en-in')
        # print(f"user say:{query}")
        # speak(query)
    except Exception as e:
        # print(e)
        speak("I can't understand ")
        return 'none'
    return query

def news():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=efa0ddd8997f417fa23a08f8ee62633b"
    news = requests.get(url).text

    # print(news["articles"])
    # head = news["articles"]
    for i in range(0, 5):
        if i < 4:
            speak(news["articles"][i]["title"])
            # print(news["articles"][i]["title"])


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

def hello(event):
    while True:
        query = takecommand().lower()
        # every logic possiable
        if 'wikipedia' in query:
            # print('searching on wikipedia...')
            speak('searching on wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            # print(result)
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
            # print(song)
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
                # print(e)
                speak('sir! i am NOT  able to access')

# if __name__=="__main__":
#     # wishme()
#     # speak('arfaan mera babu hai lalalalalalal')
#     while True:
#         query = takecommand().lower()
#         # every logic possiable
#         if 'wikipedia' in query:
#             print('searching on wikipedia...')
#             speak('searching on wikipedia...')
#             query = query.replace('wikipedia', '')
#             result = wikipedia.summary(query, sentences=2)
#             print(result)
#             speak(result)
#         elif 'who created you' in query:
#             speak('i am created by developer name saad chaudhary')
# 
#         elif 'who are you' in query:
#             speak('I am parkash')
# 
#         elif 'what is your goal' in query:
#             speak('My goal is to take world in next level of automation')
#         elif "news " in query:
#             news()
# 
#         elif 'open youtube' in query:
#             webbrowser.open('youtube.com')
# 
#         elif 'open google' in query:
#             webbrowser.open('google.com')
# 
#         elif 'play music' in query:
#             music_dir = 'E:\\soong'
#             song = os.listdir(music_dir)
#             print(song)
#             os.startfile(os.path.join(music_dir, song[0]))
#         elif 'open sublime' in query:
#             code = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
#             os.startfile(code)
#         elif 'tell time' in query:
#             time = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"sir ,Its {time}")
#         elif 'roll a dice' in query:
#             rolldices()
#         elif 'send email' in query:
#             try:
#                 speak('what should i write')
#                 content = takecommand()
#                 to = 'saadchaudhary646@gmail.com'
#                 sendemail(to, content)
#                 speak('sir email has been send')
#             except Exception as e:
#                 print(e)
#                 speak('sir! i am NOT  able to access')
#
def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text

# photo=PhotoImage(file=r"E:\parkash\kk.gif")
root = Tk()

root.title("Parkash")
root.geometry("800x500")
texts = []
photos = []
for i in range(0, 1):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.gif")
    #TODO: Resize these images
    image = image.resize((225, 265), Image.ANTIALIAS)
    photos.append(ImageTk   .PhotoImage(image))

def quuit(event):
    root.quit()
f0 = Frame(root, width=800, height=70)
Label(f0, text="Parkash ", font="lucida 33 bold").pack()
# Label(f0, text="January 19, 2050", font="lucida 13 bold").pack()
f0.pack()

l=Label(root,text="Click on button to interact with parkash",bg="orange",width=800,font="lucida 13 bold")
l.pack(fill="both")

f1 = Frame(root, width=900, height=200)
Label(f1, text=texts[0], padx=22, pady=22).pack(side="left")
Label(f1, image=photos[0]).pack()
f1.pack(fill='both')


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



back = Frame(root,bg='black')
back.pack(fill="both")

l=Label(back,text="Intract with parkash ",bg="orange")
l.pack(fill="both")

w = Button(back,text="Start",padx=50)
w.bind("<Button-1>",hello)
w.pack()

b= Button(back,text="Greet",padx=50)
b.bind("<Button-1>",wishme)
b.pack()

ll= Button(back,text="Close",padx=50)
ll.bind("<Button-1>",quuit)
ll.pack()


footer=Label(root,text="Develop by saad chaudhary.",bd=1,relief=SUNKEN,anchor="w",font="lucida 13 bold")
footer.pack(side=BOTTOM,fill=X)



root.mainloop()
