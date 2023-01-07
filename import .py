import pyttsx3
import speech_recegnition as sr
import datetime
import wikipedia
import webbrowser
import os
import snatplib

engine = pyttsx3 .init ('sapis')
voice = engine.getproperty ('voices')
# print (voice[1].id)
engine.setproperty ('voice',voice[0].id)


def speak (audio):
    engine.say(audio)
    engine.runAndwait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoom")

    else:
        speak("good evening")

        speak("i am jarvis sir. pleas tell me how my i help you")

def talkcommand():
    #it take microphone input from the user and returns sstring output.

    r= sr.recognizer()
    with sr. microphone()as source :
        print("listening....")
        r.pause_threshold=1
        audio= r.listen(source)

    try:
        print("recoghizing...")
        query = r. recognize_google(audio,language='en-in')
        print (f"user asid :{query}\n")

    except exception as e:
        #print(e)
        print ("say that again please...")
        return "none"
    return query

def sendEmail(to,content):
    server = smtplib.SMPT('smtp.gmail.com', 587)
    server.enla()
    server.starttls()
    server.login('theanjishnu@gmail.com','majoranjishnu')
    server.sendmail('theanjishnu@gail.com',to ,content)
    server.close()

if_name_ == "main"
wishme()
while true:
# if 1:
 query = takecommand().lower()

 # logic for executing tasks based on query.
 if 'wikipedia'in query:
    speak ('search wikipedia...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences=2)
    speak("according to wikipedia")
    print(result)
    speak(result)

elif'open youtube'in query:
    webbrowser.open("youtube.com")

elif'open google'in query:
    webbrowser.open("google.com")

elif'open stackoverflow'in query:
    webbrowser.open("stackoverflow.com")


elif 'play music' in query:
    music-dir='d:\\non critical\\song\\faverits songs2'
    song=os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir,song[0]))

elif'thetime'in query
     strtime=datetime.datetime.now().strftime("%H:%M:%S")
     speak(f"sir.the time is {strtime}")

elif'open code'in query:
    codepath="c:\\users\\haris\\appdata\\lead\\programs\\microsoft vs code \\.exe"
    os.startfile(codepath)

    elif'email to harry'in query
    try:
        speak("what should I say?")
        content= talkcommand()
        to ='harryyouremail@gmail.com'
        sendEmail(, content)
        speak("email has been sent!")
        except Exception as e :
            print(e)
            speak("sorry my frienf anjisnu bhai . i am not able to send this email")