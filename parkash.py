import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[0].id)



def speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<=6:
        speak('good night saad')
    elif hour>=6 and hour<=12:
        speak('good morning saad !')
    elif hour>=12 and hour<=15  :
        speak('good afternoon saad !')
    elif hour>=15:
        speak('good evening saad')
    # speak('i am you personal assitant parkash how may assist you')

def takecommand():

    r =sr.Recognizer()
    with sr.Microphone() as Source:
        print('listeing...!')
        r.pause_threshold=1
        audio = r.listen(Source)

    try:
        print('recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f"user say:{query}")
        # speak(query)
    except Exception as e:
        # print(e)
        speak('somthing went wrong sorry say that again plzz!!!!!')
        return 'none'
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('saadchaudhary646@gmail.com','65%Saadd.')
    server.sendmail('saadchaudhary646@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishme()
    # speak('arfaan mera babu hai lalalalalalal')
    while True:
        query=takecommand().lower()
        # every logic possiable
        if 'wikipedia' in query:
            print('searching on wikipedia...')
            speak('searching on wikipedia...')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'who created you' in query:
            speak('i am created by developer name saad chaudhary')

        elif 'who are you' in query:
            speak('I am parkash')

        elif 'what is your goal' in query:
            speak('My goal is to take world in next level of automation')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            music_dir='E:\\soong'
            song=os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[0]))
        elif 'open sublime' in query:
            code="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(code)
        elif'tell time' in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir ,Its {time }")
        elif 'parkash quit' in query :
            exit()

        elif 'send email' in query:
            try:
                speak('what should i write')
                content=takecommand()
                to='saadchaudhary646@gmail.com'
                sendemail(to,content)
                speak('sir email has been send')
            except Exception as e:
                print(e)
                speak('sir! i am NOT  able to access')
